# imports

import wave
import matplotlib.pyplot as plt
import numpy as np

# configuracion
numpyprecision = np.int32

# Cargar audio

audio = wave.open('.\\Temp\\sound.wav', "rb")

# Obtener datos
frecuencia = audio.getframerate()
print("Frecuencia: ", frecuencia)
cantidadMuestras = audio.getnframes()
print("Cantidad muestras: ", cantidadMuestras)
sonido = audio.readframes(-1)

audio.close()

# Duracion del audio
audio_duracion = cantidadMuestras / float(frecuencia)

# array sonido
sonido_arreglo = np.frombuffer(sonido, dtype=numpyprecision) ## ajustar los bits del int segun la calidad de la señal
print("Muestras Reales: ", len(sonido_arreglo))
if (len(sonido_arreglo) != cantidadMuestras):
    print(f"Se requiere multiplicar por {len(sonido_arreglo) / float(cantidadMuestras)} la presicion del numpy en la configuracion 'numpyprecision = {numpyprecision.__name__}'")
    exit()
times = np.linspace(0, audio_duracion, num=cantidadMuestras)

# graficaar señal de audio
plt.figure(figsize=(15,5))
plt.plot(times, sonido_arreglo)
plt.title("Señal de audio")
plt.ylabel("Señal")
plt.xlabel("Seconds")
plt.xlim(0, audio_duracion)
plt.show()

