import requests
from session_manager import SessionManager
from config.settings import BASE_API_URL
def login(username, password):
        # Send POST request to Django backend with the username and password
        response = requests.post(BASE_API_URL + "token/", json={
            "username": username,
            "password": password
        })
        # Handle response from the server
        if response.status_code == 200:
            tokens = response.json()  # Get the JWT tokens
            access_token = tokens['access']
            refresh_token = tokens['refresh']

            # Store access token, refresh token, and username in SessionManager
            session = SessionManager.get_instance()
            session.set_session_data(access_token, refresh_token, username)
            print(f'access: {session.get_access_token()}')
            print(f'refresh: {session.get_refresh_token()}')
            print(f'username: {session.get_username()}')
        elif response.status_code == 401:
            message = response.json()['detail']
            print(message)
        else:
            print('Username and password fields are required')

