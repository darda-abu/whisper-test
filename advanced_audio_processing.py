import whisper
import os
from dotenv import load_dotenv


from audio_helper import *

model = whisper.load_model("base")

input_dir = "audio_advanced_input"
output_dir = "audio_advanced_output"


load_dotenv()
xi_api = os.getenv("XI_API")


for file in os.listdir(input_dir):
    print(file)
    output_subdir = os.path.join(output_dir,file[:-4])
    if not os.path.exists(output_subdir):
        os.makedirs(output_subdir)
    audio = whisper.load_audio(os.path.join(input_dir,file))
    audio = whisper.pad_or_trim(audio)
    transcribed = transcribe(model,audio,output_subdir,file)    
    detect_language(model,audio,output_subdir,file)
    translated = translate(model,audio,output_subdir,file)
    tts_transcribed(transcribed,xi_api,output_subdir,file)
    tts_translated(translated,xi_api,output_subdir,file)



