import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='tts_helper',
    version='0.0.1',
    author='John Eicher',
    author_email='john.eicher89@gmail.com',
    description='Testing installation of Package',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/saltchicken/tts_helper',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/saltchicken/tts_helper/issues"
    # },
    # license='MIT',
    py_modules=['tts_helper'],
    install_requires=['gtts', 'pydub', 'elevenlabs', 'elevenlabslib'],
)
