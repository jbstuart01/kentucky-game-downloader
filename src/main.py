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

if __name__ == "__main__":
    # Replace this path with the directory you want to scan
    directory_path = "C:\Kentucky Games"

    # Get the list of files
    files = list_files_in_directory(directory_path)

    # Print the result
    if files:
        print("\nFiles in the directory:")
        for file in files:
            print(file)
    else:
        print("No files found in the directory.")
