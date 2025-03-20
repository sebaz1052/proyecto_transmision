import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square


<<<<<<< HEAD
def text_to_signal(text: str):
    """Devuelte el tiempo, la señal cuadrada representado ascii (8 bits) y arreglos con la información qu e
    contienen la señal en tiempos y valores"""
    binary_values = [format(ord(c), '08b') for c in text]
    binary_sequence = ''.join(binary_values)

    fs = 1000
    bit_duration = 0.01
    t_total = bit_duration * len(binary_sequence)

    t = np.linspace(0, t_total, int(fs * t_total), endpoint=False)

=======
def text_to_signal(text:str):
    """Devuelte el tiempo, la señal cuadrada representado ascii (8 bits) y arreglos con la información qu e
    contienen la señal en tiempos y valores"""
    binary_values = [format(ord(c), '08b') for c in text]
    binary_sequence = ''.join(binary_values)  

    fs = 1000  
    bit_duration = 0.01 
    t_total = bit_duration * len(binary_sequence) 

    t = np.linspace(0, t_total, int(fs * t_total), endpoint=False)


>>>>>>> 868a3fd901b4010abebeae299ca8eead30c915cb
    signal = np.zeros_like(t)
    for i, bit in enumerate(binary_sequence):
        start_idx = int(i * bit_duration * fs)
        end_idx = int((i + 1) * bit_duration * fs)
<<<<<<< HEAD
        # Nivel alto o bajo según el bit
        signal[start_idx:end_idx] = 1 if bit == '1' else 0

    sample_times = np.array(
        [(i + 0.5) * bit_duration for i in range(len(binary_sequence))])
    sample_values = np.interp(sample_times, t, signal)
=======
        signal[start_idx:end_idx] = 1 if bit == '1' else 0  # Nivel alto o bajo según el bit


    sample_times = np.array([(i + 0.5) * bit_duration for i in range(len(binary_sequence))])  
    sample_values = np.interp(sample_times, t, signal) 
>>>>>>> 868a3fd901b4010abebeae299ca8eead30c915cb

    return t, signal, sample_times, sample_values


<<<<<<< HEAD
if __name__ == '__main__':

    t, signal, sample_times, sample_values = text_to_signal('Hello world')
    m = 3  # Numero de divisiones para MPSK
    sample_values = sample_values.astype(int)
    if (len(sample_values) % m != 0):
        sample_values = np.append(
            sample_values, [0 for _ in range(m - (len(sample_values) % m))])
=======

if __name__ == '__main__':

   
    t, signal, sample_times, sample_values =  text_to_signal('Hello world')
    m = 3 #Numero de divisiones para MPSK
    sample_values = sample_values.astype(int)
    if( len(sample_values) % m != 0):
       sample_values =  np.append(sample_values, [0 for _ in range(m - (len(sample_values)%m))])
>>>>>>> 868a3fd901b4010abebeae299ca8eead30c915cb

    sample_values = sample_values.reshape(-1, m)
    print(sample_values)

<<<<<<< HEAD
    base_2 = [(1 << i) for i in range(m-1, -1, -1)]
=======
    base_2 = [(1<<i) for i in range(m-1, -1, -1)]
>>>>>>> 868a3fd901b4010abebeae299ca8eead30c915cb
    print(base_2)
    sample_values = np.dot(sample_values, base_2)
    print(sample_values)

<<<<<<< HEAD
=======

>>>>>>> 868a3fd901b4010abebeae299ca8eead30c915cb
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
<<<<<<< HEAD
=======




>>>>>>> 868a3fd901b4010abebeae299ca8eead30c915cb
