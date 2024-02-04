# Google TTS
A simply Python program for using Google's Text To Speech services.

# Requirements
Check the [official guide](https://cloud.google.com/text-to-speech/docs/libraries#client-libraries-install-python) for
updated instructions. As of 2023-11-24 all requirements are specifed in [`requirements.txt`](/requirements.txt):

```shell
pip install -r requirements.txt
```

# Authentication
You need a Google Cloud project for this to work. The official documentation is available
[here](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev).

## Local development environment
1. [Install and initialize the gcloud CLI](https://cloud.google.com/sdk/docs/install)
2. Create your credential file:
   ```
   gcloud auth application-default login
   ```
   A login screen is displayed. After you log in, your credentials are stored in the [local credential file used by ADC](https://cloud.google.com/docs/authentication/application-default-credentials#personal ).
