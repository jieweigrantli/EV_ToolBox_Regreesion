import os
from boxsdk import OAuth2

def get_oauth2_client():
    """
    Initialize and return an OAuth2 object for Box authentication.

    The access token and refresh token will be stored and managed securely
    using environment variables.

    Returns:
        OAuth2: Configured OAuth2 object for Box.
    """
    client_id = os.getenv('BOX_CLIENT_ID')
    client_secret = os.getenv('BOX_CLIENT_SECRET')
    access_token = os.getenv('BOX_ACCESS_TOKEN')
    refresh_token = os.getenv('BOX_REFRESH_TOKEN')

    if not all([client_id, client_secret, access_token, refresh_token]):
        raise EnvironmentError(
            "Missing one or more required Box credentials in environment variables."
        )

    # Callback function to store new tokens
    def store_tokens(new_access_token, new_refresh_token):
        os.environ['BOX_ACCESS_TOKEN'] = new_access_token
        os.environ['BOX_REFRESH_TOKEN'] = new_refresh_token
        print("Tokens refreshed and stored successfully.")

    # Create and return the OAuth2 client
    return OAuth2(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        refresh_token=refresh_token,
        store_tokens=store_tokens
    )