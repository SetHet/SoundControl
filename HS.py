import matplotlib.pyplot as plt

#import scikits.audiolab as audiolab
import wave
import numpy as np

#sound = audiolab.sndfile('.\\Temp\\sound.wav', 'read')
sound = wave.open('.\\Temp\\sound.wav', "rb")
#y = sound.read_frames(sound.get_nframes())
y = np.frombuffer(sound.readframes(-1), dtype=np.int32)
y = y.copy()
# for i in range(len(y)):
#     if y[i]==0:
#         y[i]=0.1
for i in range(len(y)):
    y[i] = int(y[i] / 22050.0)
    if y[i] < 0:
        y[i] = -y[i]
    if y[i] == 0:
        y[i] = 1
print(y[50000:50010])
sound.close()


Pxx, freqs, bins, im = plt.specgram(y, NFFT=512, Fs=48000)
plt.xlim(0, len(y) / 48000.0)
plt.ylim(0, 22050.0)
plt.colorbar(im).set_label(u'Intensidad (dB)')
plt.xlabel(u'Tiempo (s)')
plt.ylabel(u'Frecuencia (Hz)')