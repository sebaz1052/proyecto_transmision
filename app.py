import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

file = 'AudioPrueba.wav'

# Segmento de tiempo y canal que observaremos
chanel = 0
begin = 16000
end = 17200

# Leer el archivo, velocidad de muestreo y el sonido
# sampling: Frecuencia de muestreo
# sound: array que contiene los datos del audio
sampling, sound = waves.read(file)

# Extraer el segmento de sonido
dt = 1/sampling  # Periodo de muestreo
# Genera arreglo de valores de tiempo avanzando en intervalos de dt
ti = np.arange(begin*dt, end*dt, dt)
# Cantidad de muestras en el segmento que se va a analizar
samples = len(ti)
# Extrae el segmento de audio correspondiente a los indices deseados
segment = sound[begin: begin+samples, chanel]


# out
print('Frecuencia de muestreo:', sampling)
print('Dimensiones de sonido:', np.shape(sound))
print('Datos del sonido:')
print(sound)

print('Segmento:')
print(segment)

# Grafica
plt.plot(ti, segment)
plt.xlabel('t segundos')
plt.ylabel('Sonido(t)')
plt.show()
