# session_manager.py

class SessionManager:
    _instance = None

    def __init__(self):
        if SessionManager._instance is None:
            SessionManager._instance = self
        self.access_token = None  # To store the access token
        self.refresh_token = None  # To store the refresh token
        self.username = None  # To store the username

    @staticmethod
    def get_instance():
        if SessionManager._instance is None:
            SessionManager()
        return SessionManager._instance

    def set_session_data(self, access_token, refresh_token, username):
        """Store access token, refresh token, and username."""
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.username = username

    def get_access_token(self):
        """Retrieve the access token."""
        return self.access_token

    def get_refresh_token(self):
        """Retrieve the refresh token."""
        return self.refresh_token

    def get_username(self):
        """Retrieve the username."""
        return self.username

    def clear_session(self):
        """Clear access token, refresh token, and username."""
        self.access_token = None
        self.refresh_token = None
        self.username = None
