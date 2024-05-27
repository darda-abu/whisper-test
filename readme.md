# Audio Processing

For advanced audio processing, follow these steps:

1. Speeches are generated using ElevenLabs. Put an ElevenLabs API key in the [.env](.env) file.
2. Place audio files in the [audio_advanced_processing](audio_advanced_processing) directory.
3. Run the following command:


```bash
python .\advanced_audio_processing.py
```

4. For each audio file, a new subdirectory will be created in the [cv_advanced_output](cv_advanced_output) directory.
5. Language, transcription, and translation text files will be generated, along with Text-to-Speech (TTS) audio for the transcribed and translated text.

- Note: This process only works for `.wav` and `.mp3` files, and the generated output will be in `.mp3` format.
- Languages are in `ISO 639-1` format.
