"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import argparse
from google.cloud import texttospeech
import os

parser = argparse.ArgumentParser("tts.py")
parser.add_argument("-s", "--ssml", dest='ssml', help="The input .ssml file to get the speech data from", action='store', default="synthesis.xml")
parser.add_argument("-o", "--output", dest='output', help="The output .mp3 file to write the generated audio into", action='store', default="output.mp3")
parser.add_argument("-l", "--language-code", dest='language_code', help="The language code of the locale to use for generating the audio", action='store', default="en-US")
parser.add_argument("-v", "--voice", dest='voice', help="The voice to use for the synthesis", action='store', default="en-US-Neural2-C")
parser.add_argument("--pitch", dest='pitch', help="The pitch to use", action='store', type=float, default="0")
parser.add_argument("--rate", dest='rate', help="The speaking rate to use.", action='store', type=float, default="1")
args = parser.parse_args()

input_file: str = args.ssml
output_file: str = args.output
language_code: str = args.language_code
voice: str = args.voice
pitch: float = args.pitch
rate: float = args.rate

# First check if the file exists
if not os.path.isfile(input_file):
    print(f"There isn't any synthesis file available: {input_file}")
    exit(1)

print(f"Running voice synthesis for {input_file} in language {language_code}.")
print(f"Using voice {voice}")
print(f"Using {pitch} for pitch, and {rate} as speaking rate.")
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
    language_code=language_code,
    name=voice
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=rate,
    pitch=pitch
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# The response's audio_content is binary.
with open(output_file, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written')
