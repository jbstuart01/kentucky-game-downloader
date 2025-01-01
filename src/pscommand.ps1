yt-dlp `
  --ffmpeg-location C:\Scripts\kentucky-game-downloader\ffmpeg.exe `
  --format bestvideo+bestaudio `
  --merge-output-format mp4 `
  --write-thumbnail `
  --convert-thumbnails jpg `
  --output "C:\Kentucky Games\%(title)s.%(ext)s" `
  --download-archive "C:\Kentucky Games\downloads.txt" `
  --write-description `
  "https://www.youtube.com/watch?v=JOGQW70A_XE&list=PLW9qLa2D-k9VYQsHDJ3_jZyJ2WIs9VvXf"
