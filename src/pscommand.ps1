yt-dlp `
  --ffmpeg-location C:\Scripts\kentucky-game-downloader\ffmpeg.exe `
  --format bestvideo+bestaudio `
  --merge-output-format mp4 `
  --write-thumbnail `
  --convert-thumbnails jpg `
  --output "M:\Kentucky Games\%(title)s.%(ext)s" `
  --download-archive "M:\Kentucky Games\downloads.txt" `
  --write-description `
  --source-address 192.168.0.115 `
  "https://www.youtube.com/watch?v=JOGQW70A_XE&list=PLW9qLa2D-k9VYQsHDJ3_jZyJ2WIs9VvXf"
