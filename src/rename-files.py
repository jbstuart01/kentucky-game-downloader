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
    Separates filenames into two lists: one for '.mp4' files and one for '.txt' files.

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
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.lower().endswith('.description'):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, os.path.splitext(filename)[0] + '.txt')
            os.rename(old_path, new_path)

def convert_filename(new_date, filename):
    """
    Convert the filename by adding the formatted date in the standard format.
    
    :param new_date: The formatted date to insert into the filename.
    :param filename: The original filename to be converted.
    :return: The new filename with the date inserted.
    """
    pattern = r'^\d{4}-\d{4} - Kentucky Basketball - '
    new_filename = re.sub(pattern, f'UKMB {new_date} - ', filename)
    return new_filename

def rename_files(directory, mp4_files, description_files, formatted_dates):
    """
    Renames the files in the directory based on the provided formatted dates, 
    matching each .mp4 with its corresponding .txt and .jpg file.
    
    :param directory: The path to the directory to scan.
    :param mp4_files: The list of .mp4 filenames.
    :param description_files: The list of .txt filenames.
    :param formatted_dates: The list of formatted dates.
    """
    for i, mp4_file in enumerate(mp4_files):
        # Find the corresponding .txt file and .jpg thumbnail
        base_filename = os.path.splitext(mp4_file)[0]
        description_file = next((f for f in description_files if f.startswith(base_filename)), None)
        jpg_file = base_filename + '.jpg'
        
        if description_file and i < len(formatted_dates):
            # Get the formatted date for the current .mp4 file
            formatted_date = formatted_dates[i]
            
            # Rename the .mp4 file
            old_mp4_path = os.path.join(directory, mp4_file)
            new_mp4_filename = convert_filename(formatted_date, mp4_file)
            new_mp4_path = os.path.join(directory, new_mp4_filename)
            os.rename(old_mp4_path, new_mp4_path)
            
            # Rename the .txt file
            if description_file:
                old_description_path = os.path.join(directory, description_file)
                new_description_filename = convert_filename(formatted_date, description_file)
                new_description_path = os.path.join(directory, new_description_filename)
                os.rename(old_description_path, new_description_path)
            
            # Rename the .jpg file
            if os.path.exists(os.path.join(directory, jpg_file)):
                old_jpg_path = os.path.join(directory, jpg_file)
                new_jpg_filename = convert_filename(formatted_date, jpg_file)
                new_jpg_path = os.path.join(directory, new_jpg_filename)
                os.rename(old_jpg_path, new_jpg_path)

def main():
    directory_path = r"C:\Kentucky Games"
    change_description_to_txt(directory_path)
    
    # Step 1: Get the list of files in the directory
    files = list_files_in_directory(directory_path)

    # Step 2: Separate the files by their extension
    mp4_files, description_files = separate_files_by_extension(files)

    # Step 3: Extract formatted dates from the .txt description files
    formatted_dates = []
    for description_file in description_files:
        file_path = os.path.join(directory_path, description_file)
        formatted_date = find_and_format_date(file_path)
        if formatted_date:
            formatted_dates.append(formatted_date)

    # Step 4: Rename the files based on the formatted dates
    rename_files(directory_path, mp4_files, description_files, formatted_dates)

if __name__ == "__main__":
    main()
