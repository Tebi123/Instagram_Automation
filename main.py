from config import configure_logging
from credentials import load_credentials
from error import InstagramAutomationError
from instagram_client import login_to_instagram
from folder_manager import create_yearly_folders, load_content_into_folders
from datetime import datetime

SOURCE_DIRECTORY = "/Users/macbookpro" # Directory where new files are placed


def step1():
    """Logs into Instagram and retrieves user profile information."""
    try:
        username, password = load_credentials()
        client = login_to_instagram(username, password)

        # Example: Get your own profile information
        profile = client.user_info(client.user_id)

        print("User profile information below!")
        print(profile)

    except InstagramAutomationError as e:
        print(f"Error: {e}")


def step2():
    """Creates yearly folders based on the current year."""

    current_year = datetime.now().year  # Get the current year dynamically
    create_yearly_folders(current_year)


def main():
    step1()
    step2()

    current_year = datetime.now().year  # Get the current year dynamically
    load_content_into_folders(current_year, SOURCE_DIRECTORY)  # Automatically load files into the correct monthly folder


if __name__ == "__main__":
    configure_logging()
    main()