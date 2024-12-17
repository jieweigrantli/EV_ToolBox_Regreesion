from boxsdk import OAuth2

# Replace these with your actual credentials
CLIENT_ID = 'm12iz8095w9b7jnseufuvh7g5987hkpf'
CLIENT_SECRET = 'qpvK9j8VzHYGAFLbswellhljfHEVUmxj'
REDIRECT_URI = 'http://localhost:8080'

try:
    access_token, refresh_token = oauth2.authenticate(new_authorization_code)
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
except Exception as e:
    print(f"Failed to exchange authorization code: {e}")

def perform_oauth_flow():
    """
    Perform the full OAuth2 flow to get access and refresh tokens.
    """
    oauth2 = OAuth2(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )

    # Step 1: Get the authorization URL
    auth_url, csrf_token = oauth2.get_authorization_url(REDIRECT_URI)
    print(f"Authorize the app by visiting this URL: {auth_url}")

    # Step 2: After authorization, the user is redirected to REDIRECT_URI with a code
    # Paste the code from the redirect URL here
    authorization_code = input("Enter the authorization code from the URL: ")

    # Step 3: Exchange the authorization code for access and refresh tokens
    try:
        access_token, refresh_token = oauth2.authenticate(authorization_code)
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
        return access_token, refresh_token
    except Exception as e:
        print(f"Error during OAuth2 authentication: {e}")
        return None, None

# Call the function to perform the OAuth2 flow
perform_oauth_flow()