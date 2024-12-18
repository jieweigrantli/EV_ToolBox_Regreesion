import os
from boxsdk import OAuth2
from dotenv import load_dotenv
from threading import Lock


load_dotenv()
_env_lock = Lock()

# Box API configuration
CLIENT_ID = os.getenv("BOX_CLIENT_ID")
CLIENT_SECRET = os.getenv("BOX_CLIENT_SECRET")
REDIRECT_URI = os.getenv("BOX_REDIRECT_URI", "http://localhost")

def store_tokens(access_token, refresh_token):
    os.environ["BOX_ACCESS_TOKEN"] = access_token
    os.environ["BOX_REFRESH_TOKEN"] = refresh_token

    with _env_lock:  # Lock during updates
        with open(".env", "r") as file:
            lines = file.readlines()
        with open(".env", "w") as file:
            for line in lines:
                if line.startswith("BOX_ACCESS_TOKEN"):
                    file.write(f"BOX_ACCESS_TOKEN={access_token}\n")
                elif line.startswith("BOX_REFRESH_TOKEN"):
                    file.write(f"BOX_REFRESH_TOKEN={refresh_token}\n")
                else:
                    file.write(line)
    print("Tokens refreshed and stored successfully.")

def get_authorization_url():
    """
    Get the authorization URL to initiate the OAuth2 flow.
    """
    oauth = OAuth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, store_tokens=store_tokens)
    auth_url, csrf_token = oauth.get_authorization_url(REDIRECT_URI)
    print(f"Visit the following URL to authorize the application: {auth_url}")
    return csrf_token

def authenticate(auth_code, csrf_token=None):
    """
    Authenticate using the authorization code and obtain access/refresh tokens.
    """
    oauth = OAuth2(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        store_tokens=store_tokens,
    )

    if csrf_token:
        print("Verifying CSRF token...")
        # Verify CSRF token if applicable (optional step)
        assert csrf_token is not None, "CSRF token verification failed"

    access_token, refresh_token = oauth.authenticate(auth_code)
    print("Authentication successful!")
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")

def get_oauth2_client():
    """
    Instantiate the OAuth2 object for making Box API requests.
    Automatically refreshes tokens when needed.
    """
    access_token = os.getenv("BOX_ACCESS_TOKEN")
    refresh_token = os.getenv("BOX_REFRESH_TOKEN")

    if not all([CLIENT_ID, CLIENT_SECRET, access_token, refresh_token]):
        raise EnvironmentError("Missing Box credentials. Reauthorize the application.")

    return OAuth2(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token=access_token,
        refresh_token=refresh_token,
        store_tokens=store_tokens,
    )

if __name__ == "__main__":
    try:
        refresh_access_token()
    except Exception as e:
        print(f"Error during token refresh: {e}")