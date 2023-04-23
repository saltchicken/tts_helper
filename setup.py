from setuptools import setup, find_packages

setup(
    name="tts_helper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gtts",
        "pydub",
        "elevenlabs"
    ],
)
