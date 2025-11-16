from schemas.face_detection import OperatorUsageForecastRequest
import os
import sys
import json
import pandas as pd
import numpy as np
from utils.utils import clean_numeric_list, select_best_polynomial_model_ridge, forward_fill, backward_fill

async def handle_operator_usage_forecasting(request: OperatorUsageForecastRequest):
    # print(f"Received request: {request}")
    results = []

    for entry in request:
        operator_id = entry.operator_id

        # preprocessing data
        usage_data = clean_numeric_list(entry.last_n_days_dataset_input)
        # print(f"Processing operator_id: {operator_id}, usage_data: {usage_data}")
        usage_data = forward_fill(usage_data) # first fill forward
        usage_data = backward_fill(usage_data) # second fill backward
        # print(f"Processing operator_id: {operator_id}, usage_data: {usage_data}")

        # Convert usage_data to a pandas DataFrame
        df = pd.DataFrame(usage_data, columns=['sms_usage'])

        # Calculate statistics
        # Mean, median, min, max are useful for understanding central tendency
        mean_usage = df['sms_usage'].mean()
        median_usage = df['sms_usage'].median()
        min_usage = df['sms_usage'].min()
        max_usage = df['sms_usage'].max()

        # Prepare data for polynomial regression
        # X is the day index, y is the SMS usage
        # Reshape X to be a 2D array for sklearn
        # Using np.arange to create a range of indices for the days
        # This assumes that the input data is ordered by day
        X = np.arange(len(usage_data)).reshape(-1, 1)
        y = usage_data


        best_model, best_poly, best_degree, best_bic = select_best_polynomial_model_ridge(X, y)
                
        # Prepare data for prediction
        # Predicting for tomorrow and day after tomorrow
        # Using the polynomial features to transform the input for prediction
        X_tomorrow = best_poly.transform([[len(usage_data)]])
        X_day_after = best_poly.transform([[len(usage_data) + 1]])


        # Clip the prediction. Add a safety net: This ensures usage is not negative.
        pred_tomorrow = max(0, best_model.predict(X_tomorrow)[0])
        pred_day_after = max(0, best_model.predict(X_day_after)[0])

        result = {
            'operator_id': operator_id,
            'mean_usage': int(mean_usage),
            'median_usage': int(median_usage),
            'min_usage': int(min_usage),
            'max_usage': int(max_usage),
            'best_degree': best_degree,
            'predicted_tomorrow': int(pred_tomorrow),
            'predicted_day_after_tomorrow': int(pred_day_after),
            'best_bic': best_bic
        }

        results.append(result)

    # print(f"Processed results: {results}")
    

    return results



