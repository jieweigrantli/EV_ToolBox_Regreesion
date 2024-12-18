from token_manager import get_oauth2_client
from boxsdk import Client
from boxsdk.object.file import File
from dotenv import load_dotenv
import os

load_dotenv()

def authenticate_box(client_id, client_secret, developer_token):
    """Authenticate with Box."""
    oauth2 = get_oauth2_client()
    client = Client(oauth2)
    return client

def download_file_from_box(client, file_id, download_path):
    """
    Download a file from Box to a local path.

    Args:
        client (Client): Authenticated Box client.
        file_id (str): ID of the Box file to download.
        download_path (str): Local path to save the downloaded file.

    Returns:
        str: Local path of the downloaded file.
    """
    try:
        file = client.file(file_id).get()
        with open(download_path, 'wb') as output_file:
            file.download_to(output_file)
        print(f"File downloaded successfully: {download_path}")
        return download_path
    except Exception as e:
        print(f"Error downloading file (ID: {file_id}): {e}")
        raise

def upload_file_to_box(client, folder_id, file_path):
    """
    Upload a file to Box, overwriting the existing file if it exists.

    Args:
        client (Client): Authenticated Box client.
        folder_id (str): ID of the Box folder to upload the file to.
        file_path (str): Local path of the file to upload.

    Returns:
        file: The uploaded file object.
    """
    folder = client.folder(folder_id).get()
    file_name = os.path.basename(file_path)

    # Check if a file with the same name already exists
    existing_files = folder.get_items()
    for item in existing_files:
        if item.name == file_name:
            print(f"File with name '{file_name}' already exists. Overwriting...")
            existing_file = client.file(item.id).get()
            existing_file.delete()
            break

    # Upload the file
    uploaded_file = folder.upload(file_path)
    print(f"File uploaded successfully: {uploaded_file.name}")
    return uploaded_file