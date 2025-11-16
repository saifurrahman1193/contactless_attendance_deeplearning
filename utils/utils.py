
# 📄 File: utils.py

import numpy as np

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures

# Convert all values to float safely 
def clean_numeric_list(raw_list):
    cleaned = []
    for x in raw_list:
        try:
            cleaned.append(float(x))
        except (ValueError, TypeError):
            cleaned.append(0.0)  # default to 0 if conversion fails
    return cleaned

# BIC calculation function
def calculate_bic(n, rss, k, epsilon=1e-10):
    adjusted_rss = rss + epsilon
    return n * np.log(adjusted_rss / n) + k * np.log(n)


# Function to select the best polynomial model based on BIC
# This function fits polynomial regression models of various degrees and selects the best one based on BIC
# It returns the best model, polynomial features, degree, and BIC value.
# It can be used to forecast future values based on historical data.
def select_best_polynomial_model(X, y, degree_range=range(1, 5)):
    """
    Fits polynomial regression models of various degrees and selects the best one based on BIC.

    Args:
        X (np.ndarray): Feature array (e.g., day indices).
        y (list or np.ndarray): Target values (e.g., SMS usage).
        degree_range (range): Degrees to try. Default: 1 to 4.

    Returns:
        tuple: (best_model, best_poly, best_degree, best_bic)
    """
    best_bic = float('inf')
    best_model = None
    best_poly = None
    best_degree = None

    for degree in degree_range:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X_poly = poly.fit_transform(X)

        model = LinearRegression()
        model.fit(X_poly, y)

        y_pred = model.predict(X_poly)
        rss = np.sum((y - y_pred) ** 2)

        n = len(y)
        k = X_poly.shape[1] + 1

        bic = calculate_bic(n, rss, k)

        if bic < best_bic:
            best_bic = bic
            best_degree = degree
            best_model = model
            best_poly = poly

    return best_model, best_poly, best_degree, best_bic

# Ridge-based Polynomial Regression Model Selector
def select_best_polynomial_model_ridge(X, y, degree_range=range(1, 5), alpha=1.0):
    """
    Fits Ridge polynomial regression models of various degrees and selects the best one based on BIC.

    Args:
        X (np.ndarray): Feature array (e.g., day indices).
        y (list or np.ndarray): Target values (e.g., SMS usage).
        degree_range (range): Degrees to try. Default: 1 to 4.
        alpha (float): Ridge regularization strength.

    Returns:
        tuple: (best_model, best_poly, best_degree, best_bic)
    """
    best_bic = float('inf')
    best_model = None
    best_poly = None
    best_degree = None

    for degree in degree_range:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X_poly = poly.fit_transform(X)

        model = Ridge(alpha=alpha)  # <-- Ridge instead of LinearRegression
        model.fit(X_poly, y)

        y_pred = model.predict(X_poly)
        rss = np.sum((y - y_pred) ** 2)

        n = len(y)
        k = X_poly.shape[1] + 1  # +1 for intercept

        bic = calculate_bic(n, rss, k)

        if bic < best_bic:
            best_bic = bic
            best_degree = degree
            best_model = model
            best_poly = poly

    return best_model, best_poly, best_degree, best_bic


# ================== preprocessing =====================

# Forward Fill (ffill)
#     Fill missing values with the previous non-missing value in the same column.
#     Useful in time series or ordered data.
#     Example: [1, NaN, NaN, 4] → [1, 1, 1, 4]
def forward_fill(data):
    """
    Replace 0.0 values with the most recent non-zero value (forward fill).
    Assumes input is a list of floats.

    Args:
        data (list): List of numeric values (float or int).

    Returns:
        list: Forward-filled list.
    """
    filled = []
    last_value = 0.0
    for value in data:
        if value == 0.0:
            filled.append(last_value)
        else:
            filled.append(value)
            last_value = value
    return filled

# Backward Fill (bfill)
#     Fill missing values with the next non-missing value in the same column.
#     Useful in time series or ordered data.
#     Example: [1, NaN, NaN, 4] → [1, 4, 4, 4]
def backward_fill(data):
    """
    Replace 0.0 values with the next non-zero value (backward fill).
    Assumes input is a list of floats.

    Args:
        data (list): List of numeric values (float or int).

    Returns:
        list: Backward-filled list.
    """
    filled = data.copy()
    n = len(filled)
    for i in range(n-2, -1, -1):  # iterate backward except last element
        if filled[i] == 0.0:
            filled[i] = filled[i+1]
    return filled
