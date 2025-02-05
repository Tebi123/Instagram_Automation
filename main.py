from config import configure_logging
from credentials import load_credentials
from error import InstagramAutomationError
from instagram_client import login_to_instagram
from folder_manager import create_yearly_folders
from datetime import datetime


def main():
    """Main function to run the Instagram automation."""
    try:
        username, password = load_credentials()
        client = login_to_instagram(username, password)

        # Example: Get your own profile information
        profile = client.user_info(client.user_id)

        print("User profile information below!")
        print(profile)

    except InstagramAutomationError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    configure_logging()
    main()


def main():
    current_year = datetime.now().year  # Get the current year dynamically
    create_yearly_folders(current_year)

if __name__ == "__main__":
    main()


def main():
    current_year = datetime.now().year  # Get the current year dynamically
    source_directory = "content_source"  # Directory where new files are placed

    # Ensure the yearly folders are created
    create_yearly_folders(current_year)

    # Automatically load files into the correct monthly folder
    load_content_into_folders(current_year, source_directory)

if __name__ == "__main__":
    main()
