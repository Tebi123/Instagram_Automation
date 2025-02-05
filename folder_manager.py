import os
import shutil
import calendar
from datetime import datetime


def create_yearly_folders(year):
    """
    Creates folders for all 12 months of a given year.
    Inside each month folder, it creates daily files corresponding to that month's days.
    """
    base_directory = f"{year}_content"
    os.makedirs(base_directory, exist_ok=True)

    for month in range(1, 13):  # Loop through months (1 to 12)
        month_name = calendar.month_name[month]  # Get full month name
        month_folder = os.path.join(base_directory, month_name)
        os.makedirs(month_folder, exist_ok=True)

        days_in_month = calendar.monthrange(year, month)[1]  # Get number of days in the month

        for day in range(1, days_in_month + 1):
            file_path = os.path.join(month_folder, f"{day:02d}.jpg")
            open(file_path, "w").close()

        print(f"Folder '{month_folder}' created with {days_in_month} files.")

    print("All months and days have been created successfully.")


def load_content_into_folders(year, source_directory):
    """
    Moves content from a source directory into the appropriate month folder
    based on the file's creation date.
    """
    base_directory = f"{year}_content"
    
    if not os.path.exists(base_directory):
        print("Yearly folders not found. Creating them now...")
        create_yearly_folders(year)
    
    # Get all files from the source directory
    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)

        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            # Get file creation date
            file_creation_date = datetime.fromtimestamp(os.path.getctime(file_path))
            month_name = calendar.month_name[file_creation_date.month]
            
            # Define the destination folder
            destination_folder = os.path.join(base_directory, month_name)
            os.makedirs(destination_folder, exist_ok=True)  # Ensure folder exists

            # Move the file to the correct folder
            new_file_path = os.path.join(destination_folder, file_name)
            shutil.move(file_path, new_file_path)

            print(f"Moved {file_name} to {destination_folder}")

    print("All files have been sorted into their respective month folders.")