from dotenv import load_dotenv
import os
from box_utils import download_file_from_box, upload_file_to_box
from regression_utils import perform_regression
from token_manager import get_oauth2_client

# Load environment variables from the .env file
load_dotenv()

def main():
    # Authenticate with Box using OAuth2 client
    oauth2 = get_oauth2_client()
    client = oauth2.client()

    # File and folder IDs from environment variables
    file_id = os.getenv('BOX_FILE_ID')
    folder_id = os.getenv('BOX_FOLDER_ID')

    # Local file paths for processing
    local_csv_path = 'data/input.csv'   # Temporary path for download
    local_xlsx_path = 'data/output.xlsx'  # Path for processed file output

    # Columns for regression
    target_col = os.getenv('TARGET_COLUMN')  # Target column from .env
    feature_cols = os.getenv('FEATURE_COLUMNS').split(',')  # Comma-separated feature columns

    # Step 1: Download file from Box
    download_file_from_box(client, file_id, local_csv_path)

    # Step 2: Perform regression analysis
    perform_regression(local_csv_path, local_xlsx_path, target_col, feature_cols)

    # Step 3: Upload the processed file back to Box
    upload_file_to_box(client, folder_id, local_xlsx_path)

    print("Workflow completed successfully!")

if __name__ == "__main__":
    main()