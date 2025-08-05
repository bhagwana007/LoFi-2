import os
from pylivestream import Livestream

STREAM_KEY = os.getenv("STREAM_KEY")
STREAM_URL = os.getenv("STREAM_URL", "rtmp://a.rtmp.youtube.com/live2")
AUDIO_URL = os.getenv("AUDIO_FILE")
THUMBNAIL = os.getenv("THUMBNAIL")

if not STREAM_KEY or not AUDIO_URL:
    raise Exception("STREAM_KEY and AUDIO_FILE must be set")

livestream = Livestream(
    audio_input=AUDIO_URL,
    audio_loop=True,
    title="24/7 Music Live",
    stream_url=f"{STREAM_URL}/{STREAM_KEY}",
    loglevel="info",
    thumbnail=THUMBNAIL
)

livestream.start()
