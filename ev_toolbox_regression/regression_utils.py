import pandas as pd
from sklearn.linear_model import LinearRegression

def perform_regression(combined_data, output_csv_path, target_col, feature_cols):
    """
    Perform regression and save results.

    Parameters:
        combined_data (pd.DataFrame): Combined dataset for regression.
        output_csv_path (str): Path to save the output CSV file.
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

    # Add predictions to the DataFrame
    combined_data['predictions'] = model.predict(X)

    # Save results to CSV
    combined_data.to_csv(output_csv_path, index=False)

    print("Regression completed successfully. Results saved.")
    return model