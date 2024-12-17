import os
from boxsdk import OAuth2
from dotenv import load_dotenv

load_dotenv()

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
        print(f"New Access Token: {new_access_token}")
        print(f"New Refresh Token: {new_refresh_token}")
        os.environ['BOX_ACCESS_TOKEN'] = new_access_token
        os.environ['BOX_REFRESH_TOKEN'] = new_refresh_token

        # Update the .env file with new tokens
        with open('.env', 'r') as file:
            lines = file.readlines()

        with open('.env', 'w') as file:
            for line in lines:
                if line.startswith('BOX_ACCESS_TOKEN'):
                    file.write(f"BOX_ACCESS_TOKEN={new_access_token}\n")
                elif line.startswith('BOX_REFRESH_TOKEN'):
                    file.write(f"BOX_REFRESH_TOKEN={new_refresh_token}\n")
                else:
                    file.write(line)

        print("Tokens refreshed and stored successfully.")

    # Create and return the OAuth2 client
    return OAuth2(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        refresh_token=refresh_token,
        store_tokens=store_tokens  # Handles token updates
    )