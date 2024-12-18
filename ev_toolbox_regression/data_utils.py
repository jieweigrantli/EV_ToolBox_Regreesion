import pandas as pd

def combine_datasets(file_paths):
    """
    Combine multiple datasets using the 'No' column as the key.

    Parameters:
        file_paths (list of str): List of file paths to the datasets to combine.

    Returns:
        pd.DataFrame: Combined dataset.
    """
    # Ensure at least two files are provided
    if len(file_paths) < 2:
        raise ValueError("At least two file paths are required to combine datasets.")

    # Load datasets and ensure 'No' column is consistent
    datasets = [pd.read_csv(file_path) for file_path in file_paths]

    for i, dataset in enumerate(datasets):
        if "No" not in dataset.columns:
            raise ValueError(f"'No' column missing in dataset {file_paths[i]}")
        # Ensure 'No' is of the same type across datasets
        datasets[i]["No"] = datasets[i]["No"].astype(str)

    # Merge datasets on 'No' column
    combined_data = datasets[0]
    for dataset in datasets[1:]:
        combined_data = pd.merge(combined_data, dataset, on="No", how="inner")

    print("Datasets combined successfully.")
    return combined_data