import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def perform_regression(combined_data, output_csv_path, target_col, feature_cols):
    """
    Perform regression, save coefficients to a single-row CSV, and display model statistics.

    Parameters:
        combined_data (pd.DataFrame): Combined dataset for regression.
        output_csv_path (str): Path to save the regression coefficients CSV file.
        target_col (str): Target column name for regression.
        feature_cols (list of str): List of feature column names for regression.

    Returns:
        model: Trained regression model.
    """
    # Validate the combined dataset
    missing_cols = [col for col in [target_col] + feature_cols if col not in combined_data.columns]
    if missing_cols:
        raise ValueError(f"One or more specified columns are missing in the combined dataset: {missing_cols}")

    # Fit regression model
    X = combined_data[feature_cols]
    y = combined_data[target_col]
    model = LinearRegression()
    model.fit(X, y)

    # Predict and calculate statistics
    predictions = model.predict(X)
    r2 = r2_score(y, predictions)
    mse = mean_squared_error(y, predictions)
    rmse = mse ** 0.5

    print("Regression Statistics:")
    print(f"R² Score: {r2:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}")

    # Prepare coefficients as a single-row DataFrame
    coefficients = {feature: coef for feature, coef in zip(feature_cols, model.coef_)}
    coefficients['Intercept'] = model.intercept_
    coefficients_df = pd.DataFrame([coefficients])

    # Save coefficients to CSV
    coefficients_df.to_csv(output_csv_path, index=False)

    print(f"Regression coefficients saved to {output_csv_path}.")
    return model