import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100

seconds = 3

record = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write('kayıt1.wav',fs,record)
