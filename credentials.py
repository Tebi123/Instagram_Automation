import os
from dotenv import load_dotenv
from error import EnvironmentVariableError


def load_credentials():
    """Load Instagram credentials from environment variables."""
    load_dotenv()
    
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    if not username or not password:
        raise EnvironmentVariableError("Instagram username or password not found in environment variables.")
    
    return username, password