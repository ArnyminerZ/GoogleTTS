"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os
import sys
import getopt

input_file: str | None = None
output_file: str | None = None
language_code: str | None = None

# Get all arguments
opts, args = getopt.getopt(sys.argv, "hs:o:l:", ["ssml=", "output=", "language-code="])
for opt, arg in opts:
    if opt == '-h':
        print('tts.py -s [ssml input file] -o [output mp3 file] -l [language code]')
        sys.exit()
    elif opt in ("-s", "--ssml"):
        input_file = arg
    elif opt in ("-o", "--output"):
        output_file = arg
    elif opt in ("-l", "--language-code"):
        output_file = arg

directory = os.path.dirname(__file__)

if input_file is None:
    input_file = os.path.join(directory, "synthesis.xml")
if output_file is None:
    output_file = os.path.join(directory, "output.mp3")
if language_code is None:
    language_code = "en-US"

# First check if the file exists
if not os.path.isfile(input_file):
    print(f"There isn't any synthesis file available: {input_file}")
    exit(1)

print(f"Running voice synthesis for {input_file} in language {language_code}.")
print(f"It will be stored in {output_file}")

file = open(input_file, "r")
ssml = file.read()

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(output_file, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written')
