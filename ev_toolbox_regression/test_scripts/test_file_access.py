from boxsdk import Client, OAuth2

# Replace with your credentials and file ID
CLIENT_ID = 'm12iz8095w9b7jnseufuvh7g5987hkpf'
CLIENT_SECRET = 'qpvK9j8VzHYGAFLbswellhljfHEVUmxj'
DEVELOPER_TOKEN = 'PvjzHsIiMCNKdxobBhsGp96NnmAIjzGo'
FILE_ID = '1726270708332'

def test_file_access():
    oauth2 = OAuth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=DEVELOPER_TOKEN)
    client = Client(oauth2)

    try:
        file = client.file(FILE_ID).get()
        print(f"File name: {file.name}")
        print(f"File size: {file.size} bytes")
    except Exception as e:
        print(f"File access failed: {e}")

if __name__ == "__main__":
    test_file_access()