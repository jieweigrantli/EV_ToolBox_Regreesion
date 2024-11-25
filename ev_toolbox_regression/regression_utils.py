import pandas as pd
from sklearn.linear_model import LinearRegression

def perform_regression(input_csv_paths, output_xlsx_path, target_col, feature_cols):
    """
    Perform regression and save results.

    Parameters:
        input_csv_paths (list of str): List of file paths to CSV files to combine.
        output_xlsx_path (str): Path to save the output Excel file.
        target_col (str): Target column name for regression.
        feature_cols (list of str): List of feature column names for regression.

    Returns:
        model: Trained regression model.
    """
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    # Load and combine datasets
    combined_data = pd.concat([pd.read_csv(file) for file in input_csv_paths], ignore_index=True)

    # Validate the combined dataset
    if not all(col in combined_data.columns for col in [target_col] + feature_cols):
        raise ValueError("One or more specified columns are missing in the combined dataset.")

    # Fit regression model
    X = combined_data[feature_cols]
    y = combined_data[target_col]
    model = LinearRegression()
    model.fit(X, y)

    # Add predictions to the DataFrame
    combined_data['predictions'] = model.predict(X)

    # Save results to Excel
    combined_data.to_excel(output_xlsx_path, index=False)

    return model