import os
import re

def list_files_in_directory(directory):
    """
    List all files in the given directory.

    :param directory: The path to the directory to scan.
    :return: A list of filenames in the directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            return []

        # List all files in the directory
        filenames = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return filenames

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def separate_files_by_extension(filenames):
    """
    Separates filenames into two lists: one for '.mp4' files and one for '.description' files.

    :param filenames: A list of filenames.
    :return: A tuple containing two lists: (mp4_files, description_files).
    """
    mp4_files = [file for file in filenames if file.lower().endswith('.mp4')]
    description_files = [file for file in filenames if file.lower().endswith('.txt')]
    
    return mp4_files, description_files

def find_and_format_date(file_path):
    """
    Finds the first date in MM/DD/YYYY format in a text file and returns it as YYYY-MM-DD.

    :param file_path: The path to the text file.
    :return: The date in YYYY-MM-DD format, or None if no date is found.
    """
    date_pattern = r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b'  # Matches dates in MM/DD/YYYY format

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(date_pattern, line)
            if match:
                # Extract month, day, and year
                month, day, year = match.groups()
                # Format as YYYY-MM-DD
                return f"{year}-{int(month):02d}-{int(day):02d}"

    return None

def change_description_to_txt(directory):
    """
    Changes the file extension of all '.description' files in the given directory to '.txt'.

    :param directory: The path to the directory to scan.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a '.description' extension
        if filename.lower().endswith('.description'):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, os.path.splitext(filename)[0] + '.txt')

            # Rename the file
            os.rename(old_path, new_path)

if __name__ == "__main__":
    # Replace this path with the directory you want to scan
    directory_path = "C:\Kentucky Games"

    # change the .description files to .txt
    change_description_to_txt(directory_path)

    # Get the list of files
    files = list_files_in_directory(directory_path)

    # separate the list of file names into .mp4 and .txt
    mp4_files, description_files = separate_files_by_extension(files)

    # list to hold the formatted dates
    formatted_dates = []

    # obtain the correctly formatted date from the video description
    for file in description_files:
        formatted_dates.append(find_and_format_date(f"{directory_path}\{file}"))