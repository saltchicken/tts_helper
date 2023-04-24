from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from elevenlabslib import *
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ELEVENLABS_KEY")

def say_gTTS(text, lang = "en"):
    tts = gTTS(text=text, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)

def say_elvenlabs(text):
    user = ElevenLabsUser(API_KEY)
    voice = user.get_voices_by_name("Rachel")[0]
    voice.generate_and_play_audio(text, playInBackground=False)