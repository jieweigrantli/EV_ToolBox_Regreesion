from dotenv import load_dotenv
import os
from box_utils import download_file_from_box, upload_file_to_box
from regression_utils import perform_regression
from token_manager import get_oauth2_client
from data_utils import combine_datasets

# Load environment variables from the .env file
load_dotenv()

def main():
    # Authenticate with Box using OAuth2 client
    oauth2 = get_oauth2_client()
    client = oauth2.client()

    # Parse folder-file pairs from environment variables
    folder_file_pairs = os.getenv('BOX_FOLDER_FILE_IDS').split(',')
    folder_file_pairs = [pair.split(':') for pair in folder_file_pairs]  # Split into [folder_id, file_id]

    # Output folder ID
    output_folder_id = os.getenv('BOX_OUTPUT_FOLDER_ID')

    # Temporary local file paths
    local_file_paths = [f"data/input_file_{i}.csv" for i in range(len(folder_file_pairs))]
    combined_csv_path = 'data/combined_input.csv'
    local_xlsx_path = 'data/output.xlsx'

    # Columns for regression
    target_col = os.getenv('TARGET_COLUMN')  # Target column from .env
    feature_cols = os.getenv('FEATURE_COLUMNS').split(',')  # Comma-separated feature columns

    # Step 1: Download files from Box
    for (folder_id, file_id), local_path in zip(folder_file_pairs, local_file_paths):
        download_file_from_box(client, file_id, local_path)

    # Step 2: Combine datasets into a single file
    combined_data = combine_datasets(local_file_paths)
    combined_data.to_csv(combined_csv_path, index=False)  # Save combined data temporarily

    # Step 3: Perform regression analysis
    perform_regression(combined_csv_path, local_xlsx_path, target_col, feature_cols)

    # Step 4: Upload the processed file back to Box
    upload_file_to_box(client, output_folder_id, local_xlsx_path)

    print("Workflow completed successfully!")

if __name__ == "__main__":
    main()