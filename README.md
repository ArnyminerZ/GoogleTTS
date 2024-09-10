# Google TTS
A simply Python program for using Google's Text To Speech services.

# Requirements
Check the [official guide](https://cloud.google.com/text-to-speech/docs/libraries#client-libraries-install-python) for
updated instructions. As of 2023-11-24 all requirements are specifed in [`requirements.txt`](/requirements.txt):

```shell
pip install -r requirements.txt
```

## Authentication
You need a Google Cloud project for this to work. The official documentation is available
[here](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev).

### Local development environment
1. [Install and initialize the gcloud CLI](https://cloud.google.com/sdk/docs/install)
   
   1.1. Windows:
   ```powershell
   (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/", "$env:Temp\GoogleCloudSDKInstaller.exe")

   & $env:Temp\GoogleCloudSDKInstaller.exe
   ```
2. Create your credential file:
   ```
   gcloud auth application-default login
   ```
   A login screen is displayed. After you log in, your credentials are stored in the [local credential file used by ADC](https://cloud.google.com/docs/authentication/application-default-credentials#personal ).

# Using the script
Once all the requirements have been met, you can start using the script.

You can always use `python tts.py -h` to get help about the options available. Those are:
- `-s`/`--ssml`: the input _.ssml_ file to get the speech data from (see [docs](https://cloud.google.com/text-to-speech/docs/ssml)).
  Default: `synthesis.xml`
- `-o`/`--output`: the output _.mp3_ file to write the generated audio into.
  Default: `output.mp3`
- `-l`/`--language-code`: the language code of the locale to use for generating the audio.
  Default: `en-US`

Example:
```shell
python3 tts.py -s data.ssml -o audio.mp3 -l es-ES
```
_Generates the audio from data.ssml, into audio.mp3, in Spanish from Spain._
