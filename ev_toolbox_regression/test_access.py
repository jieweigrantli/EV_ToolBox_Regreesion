from boxsdk import Client, OAuth2
import os

# Replace with your credentials
CLIENT_ID = 'm12iz8095w9b7jnseufuvh7g5987hkpf'
CLIENT_SECRET = 'qpvK9j8VzHYGAFLbswellhljfHEVUmxj'
DEVELOPER_TOKEN = 'PvjzHsIiMCNKdxobBhsGp96NnmAIjzGo'

def test_authentication():
    oauth2 = OAuth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=DEVELOPER_TOKEN)
    client = Client(oauth2)

    try:
        user = client.user().get()
        print(f"Authenticated User: {user.name} (ID: {user.id})")
    except Exception as e:
        print(f"Authentication failed: {e}")

if __name__ == "__main__":
    test_authentication()