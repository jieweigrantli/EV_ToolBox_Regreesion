from boxsdk import Client, OAuth2
from dotenv import load_dotenv

load_dotenv()

def authenticate_box(client_id, client_secret, developer_token):
    """Authenticate with Box."""
    oauth2 = OAuth2(client_id, client_secret, access_token=developer_token)
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
        print(f"Error downloading file: {e}")
        raise

def upload_file_to_box(client, folder_id, file_path):
    """Upload a file to Box."""
    folder = client.folder(folder_id).get()
    file_name = file_path.split('/')[-1]
    uploaded_file = folder.upload(file_path, file_name)
    return uploaded_file