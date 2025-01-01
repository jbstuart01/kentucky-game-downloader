import os

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
    description_files = [file for file in filenames if file.lower().endswith('.description')]
    
    return mp4_files, description_files

if __name__ == "__main__":
    # Replace this path with the directory you want to scan
    directory_path = "C:\Kentucky Games"

    # Get the list of files
    files = list_files_in_directory(directory_path)

    # separate the list of file names into .mp4 and .description
    mp4_files, description_files = separate_files_by_extension(files)
    
