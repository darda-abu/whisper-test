import whisper
import os
import requests

def transcribe(model,audio,output_dir,file):
    result = model.transcribe(audio)
    with open(os.path.join(output_dir, file[:-4]+"_transcribed.txt"), "w",encoding="utf-8") as f:
        f.write(result["text"])
    return result["text"]

def detect_language(model,audio,output_dir,file):
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    with open(os.path.join(output_dir, file[:-4]+"_language.txt"), "w",encoding="utf-8") as f:
        f.write(max(probs, key=probs.get))

def translate(model,audio,output_dir,file):
    translated = model.transcribe(audio, language="en", task="translate")
    with open(os.path.join(output_dir, file[:-4]+"_translated.txt"), "w",encoding="utf-8") as f:
        f.write(translated["text"])
    return translated["text"]

def tts(text,api,output_dir):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    with open(output_dir, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

def tts_transcribed(transcribed, api, output_dir,file):
    tts(transcribed,api,os.path.join(output_dir, file[:-4]+"_tts_trancribed.mp3"))

def tts_translated(translated, api, output_dir,file):
    tts(translated,api,os.path.join(output_dir, file[:-4]+"_tts_translated.mp3"))
