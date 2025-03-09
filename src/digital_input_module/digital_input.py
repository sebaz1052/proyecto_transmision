import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square


def text_to_signal(text:str):

    binary_values = [format(ord(c), '08b') for c in text]
    binary_sequence = ''.join(binary_values)  

    fs = 1000  # Frecuencia de muestreo para la señal continua
    bit_duration = 0.01  # Duración de cada bit en segundos
    t_total = bit_duration * len(binary_sequence)  # Tiempo total

    t = np.linspace(0, t_total, int(fs * t_total), endpoint=False)


    signal = np.zeros_like(t)
    for i, bit in enumerate(binary_sequence):
        start_idx = int(i * bit_duration * fs)
        end_idx = int((i + 1) * bit_duration * fs)
        signal[start_idx:end_idx] = 1 if bit == '1' else 0  # Nivel alto o bajo según el bit

    # *** MUESTREO EN LA MITAD DEL PERIODO ***
    sample_times = np.array([(i + 0.5) * bit_duration for i in range(len(binary_sequence))])  # Mitad de cada bit
    sample_values = np.interp(sample_times, t, signal)  # Obtener valores en esos instantes

    return t, signal, sample_times, sample_values



if __name__ == '__main__':
    # Graficar la señal original y los puntos muestreados
   
    t, signal, sample_times, sample_values =  text_to_signal('Hello world')
    m = 3 #Numero de divisiones para MPSK
    sample_values = sample_values.astype(int)
    if( len(sample_values) % m != 0):
       sample_values =  np.append(sample_values, [0 for _ in range(m - (len(sample_values)%m))])

    sample_values = sample_values.reshape(-1, m)
    print(sample_values)

    base_2 = [(1<<i) for i in range(m-1, -1, -1)]
    print(base_2)
    sample_values = np.dot(sample_values, base_2)
    print(sample_values)


    # plt.figure(figsize=(10, 4))
    # plt.plot(t, signal, label="Señal binaria")
    # plt.scatter(sample_times, sample_values, color='red', label="Muestras (mitad del bit)", zorder=3)
    # plt.xlabel("Tiempo (s)")
    # plt.ylabel("Amplitud")
    # plt.title("Muestreo en la mitad del periodo de cada bit")
    # plt.yticks([0, 1], ['0', '1'])
    # plt.legend()
    # plt.grid()
    # plt.show()




