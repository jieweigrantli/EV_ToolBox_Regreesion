from boxsdk import Client, OAuth2

def authenticate_box(client_id, client_secret, developer_token):
    """Authenticate with Box."""
    oauth2 = OAuth2(client_id, client_secret, access_token=developer_token)
    client = Client(oauth2)
    return client

def download_file_from_box(client, file_id, download_path):
    """Download a file from Box."""
    file = client.file(file_id).get()
    with open(download_path, 'wb') as output_file:
        file.download_to(output_file)

def upload_file_to_box(client, folder_id, file_path):
    """Upload a file to Box."""
    folder = client.folder(folder_id).get()
    file_name = file_path.split('/')[-1]
    uploaded_file = folder.upload(file_path, file_name)
    return uploaded_file