import wave
import os

# os.makedirs("media_files",exist_ok=True)
# os.chdir("media_files")
# audio_file=[]
# for files in os.listdir("."):
#     if (files.endswith(".mp3")) or (files.endswith(".wav")):
#         audio_file.append(files)
# audio_file.sort(key=os.path.getctime)

# print(audio_file)

# obj=wave.open(audio_file[0],'rb')
# print("Number of Channels",obj.getnchannels())
# print("Sample Width",obj.getsampwidth())
# print("Frame Rate",obj.getframerate())
# print("Number of Frames",obj.getnframes())
# print("Parameters",obj.getparams())

import librosa
import soundfile as sf
x,_ = librosa.load('media_files\Eladio Carrion, Bad Bunny - Coco Chanel.mp3', sr=16000)
sf.write('tmp.wav', x, 16000)
wave.open('tmp.wav','r')