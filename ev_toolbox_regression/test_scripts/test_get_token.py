from boxsdk import OAuth2
import os
from dotenv import load_dotenv

load_dotenv()

# Replace these with your credentials
client_id = os.getenv('BOX_CLIENT_ID')
client_secret = os.getenv('BOX_CLIENT_SECRET')
access_token = os.getenv('BOX_ACCESS_TOKEN')
refresh_token = os.getenv('BOX_REFRESH_TOKEN')

def refresh_box_tokens(client_id, client_secret, refresh_token):
    """
    Refresh Box tokens using the provided refresh token.

    Args:
        client_id (str): Your Box app's client ID.
        client_secret (str): Your Box app's client secret.
        refresh_token (str): Your current refresh token.

    Returns:
        dict: A dictionary containing the new access_token and refresh_token.
    """
    oauth2 = OAuth2(
        client_id=client_id,
        client_secret=client_secret,
        access_token=None,
        refresh_token=refresh_token,
    )

    try:
        # Trigger a token refresh
        new_access_token, new_refresh_token = oauth2.refresh(None)
        print(f"New Access Token: {new_access_token}")
        print(f"New Refresh Token: {new_refresh_token}")

        # Optionally, store the tokens securely
        os.environ['BOX_ACCESS_TOKEN'] = new_access_token
        os.environ['BOX_REFRESH_TOKEN'] = new_refresh_token

        return {"access_token": new_access_token, "refresh_token": new_refresh_token}
    except Exception as e:
        print(f"Failed to refresh tokens: {e}")
        return None

if __name__ == "__main__":
    tokens = refresh_box_tokens(client_id, client_secret, refresh_token)
    if tokens:
        print("Tokens refreshed successfully.")
    else:
        print("Failed to refresh tokens.")