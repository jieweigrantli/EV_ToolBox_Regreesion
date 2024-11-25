import pandas as pd

def combine_datasets(file_paths, ignore_index=True):
    """
    Combine multiple datasets into a single DataFrame.

    Parameters:
        file_paths (list of str): List of file paths to CSV files.
        ignore_index (bool): Whether to ignore index while combining.

    Returns:
        pd.DataFrame: Combined dataset.
    """
    return pd.concat([pd.read_csv(file) for file in file_paths], ignore_index=ignore_index)