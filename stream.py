import os
import subprocess

# Get environment variables
stream_key = os.getenv("STREAM_KEY")
stream_url = os.getenv("STREAM_URL", "rtmp://a.rtmp.youtube.com/live2")
audio_file = os.getenv("AUDIO_FILE")
thumbnail = os.getenv("THUMBNAIL")

if not all([stream_key, audio_file, thumbnail]):
    raise Exception("Missing required environment variables.")

# Final RTMP destination
rtmp_url = f"{stream_url}/{stream_key}"

# FFmpeg Command
command = [
    "ffmpeg",
    "-re",
    "-loop", "1",
    "-i", thumbnail,
    "-stream_loop", "-1",
    "-i", audio_file,
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-tune", "stillimage",
    "-c:a", "aac",
    "-b:a", "128k",
    "-pix_fmt", "yuv420p",
    "-shortest",
    "-f", "flv",
    rtmp_url
]

# Run the command
subprocess.run(command)
