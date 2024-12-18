from dotenv import load_dotenv
import os
from token_manager import get_oauth2_client, authenticate, get_authorization_url
from boxsdk import Client
from box_utils import download_file_from_box, upload_file_to_box
from data_utils import combine_datasets
from regression_utils import perform_regression

load_dotenv()

def main():
    # Ensure we have valid tokens
    try:
        oauth2 = get_oauth2_client()
    except EnvironmentError as e:
        print(str(e))
        print("Reauthorizing the application...")
        csrf_token = get_authorization_url()
        auth_code = input("Enter the authorization code you received: ")
        authenticate(auth_code, csrf_token)
        oauth2 = get_oauth2_client()

    # Create authenticated client
    client = Client(oauth2)

    try:
        user = client.user().get()
        print(f"Authenticated User: {user.name} (ID: {user.id})")
    except Exception as e:
        print("Authentication failed. Reauthorize the application.")
        csrf_token = get_authorization_url()
        auth_code = input("Enter the new authorization code you received: ")
        authenticate(auth_code, csrf_token)
        oauth2 = get_oauth2_client()
        client = Client(oauth2)

# Parse file IDs and output folder ID
    file_ids = os.getenv('BOX_FILE_IDS', '').split(',')
    if not file_ids:
        print("No file IDs provided in BOX_FILE_IDS.")
        return

    output_folder_id = os.getenv('BOX_OUTPUT_FOLDER_ID')

    # Temporary local file paths
    local_file_paths = [f"data/input_file_{i}.csv" for i in range(len(file_ids))]
    combined_csv_path = 'data/combined_input.csv'
    local_csv_path = 'data/reg_coefficients.csv'

    target_col = os.getenv('TARGET_COLUMN')
    feature_cols = os.getenv('FEATURE_COLUMNS', '').split(',')

    # Step 1: Download files from Box
    for file_id, local_path in zip(file_ids, local_file_paths):
        download_file_from_box(client, file_id, local_path)

    # Step 2: Combine datasets
    combined_data = combine_datasets(local_file_paths)
    combined_data.to_csv(combined_csv_path, index=False)

    # Step 3: Perform regression
    perform_regression(combined_data, local_csv_path, target_col, feature_cols)

    # Step 4: Upload results back to Box
    upload_file_to_box(client, output_folder_id, local_csv_path)

    print("Workflow completed successfully!")

if __name__ == "__main__":
    main()