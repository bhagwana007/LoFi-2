import os
import subprocess

stream_key = os.getenv("STREAM_KEY")
song_url = os.getenv("SONG_URL")
thumbnail = os.getenv("THUMBNAIL")

cmd = [
    "ffmpeg",
    "-re",
    "-loop", "1",
    "-i", thumbnail,
    "-i", song_url,
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-maxrate", "3000k",
    "-bufsize", "6000k",
    "-pix_fmt", "yuv420p",
    "-g", "50",
    "-c:a", "aac",
    "-b:a", "128k",
    "-shortest",
    "-f", "flv",
    f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"
]

print("🔴 Streaming started...")
subprocess.run(cmd)
