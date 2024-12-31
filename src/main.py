import os
import re
import yt_dlp

def extract_date_from_description(description):
    """Extract and format a date from a video's description."""
    # Regular expression to find MM/DD/YYYY dates
    date_regex = r'\b(\d{2})/(\d{2})/(\d{4})\b'
    date_match = re.search(date_regex, description)

    if date_match:
        # Convert MM/DD/YYYY to YYYY-MM-DD
        return f"{date_match.group(3)}-{date_match.group(1)}-{date_match.group(2)}"
    return None


# URL of the playlist
if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/watch?v=JOGQW70A_XE&list=PLW9qLa2D-k9VYQsHDJ3_jZyJ2WIs9VvXf"