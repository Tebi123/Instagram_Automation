import logging
from instagrapi import Client
from instagrapi.exceptions import UnknownError
from error import AuthenticationError, InstagramAutomationError


def login_to_instagram(username, password):
    """Login to Instagram using the provided credentials."""
    client = Client()
    
    try:
        client.login(username, password)
        logging.info("Successfully logged in to Instagram.")

    except UnknownError as e:
        logging.error(f"Login failed: {e}")
        raise AuthenticationError("Failed to log in to Instagram. Please check your credentials.")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise InstagramAutomationError("An unexpected error occurred during login.")
    

    return client