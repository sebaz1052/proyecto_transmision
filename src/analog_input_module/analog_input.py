import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

def anolog_input_wav(file, channel=0, begin=0, end=17200):
    """
    Lee un archivo de audio WAV y extrae un segmento específico.
    Retorna los tiempos, los valores del audio en ese intervalo y grafica la señal.
    
    Parámetros:
    file (str): Ruta del archivo de audio.
    channel (int): Canal a analizar (por defecto, 0 para audio estéreo).
    begin (int): Índice de inicio del segmento.
    end (int): Índice de fin del segmento.
    
    Retorna:
    tuple: (tiempos, valores de audio)
    """
    
    sampling, sound = waves.read(file)
    if end == -1:
        end = len(sound)

    if len(sound.shape) == 1:  # Audio mono
        segment = sound[begin:end]
    else:  
        segment = sound[begin:end, channel]

    dt = 1 / sampling
    ti = np.arange(begin * dt, end * dt, dt)[:len(segment)]
    
    return ti, segment
