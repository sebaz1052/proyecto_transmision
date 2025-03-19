import numpy as np
import matplotlib.pyplot as plt


def text_to_signal(text: str):
    """
    Convierte un texto en su representación binaria (en 8 bits por carácter) y genera
    una señal digital continua con cada bit representado durante un intervalo de tiempo.
    Además, se extraen los valores de muestreo a la mitad de cada bit.
    """
    # Convertir cada carácter a su representación de 8 bits y concatenarlos
    binary_values = [format(ord(c), '08b') for c in text]
    binary_sequence = ''.join(binary_values)

    fs = 1000            # Frecuencia de muestreo (Hz)
    bit_duration = 0.01    # Duración de cada bit (s)
    t_total = bit_duration * len(binary_sequence)
    t = np.linspace(0, t_total, int(fs * t_total), endpoint=False)

    # Crear la señal digital: para cada bit se asigna 1 o 0 durante el intervalo correspondiente
    digital_signal = np.zeros_like(t)
    for i, bit in enumerate(binary_sequence):
        start_idx = int(i * bit_duration * fs)
        end_idx = int((i + 1) * bit_duration * fs)
        digital_signal[start_idx:end_idx] = 1 if bit == '1' else 0

    # Muestrear en el centro de cada bit
    sample_times = np.array(
        [(i + 0.5) * bit_duration for i in range(len(binary_sequence))])
    sample_values = np.interp(sample_times, t, digital_signal)

    return t, digital_signal, sample_times, sample_values


if __name__ == '__main__':
    t, sig, sample_times, sample_vals = text_to_signal("Hello AM")
    plt.figure(figsize=(10, 4))
    plt.plot(t, sig, label="Señal Digital (0/1)")
    plt.scatter(sample_times, sample_vals, color='red',
                label="Muestras (centro de bit)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Señal de entrada digital para AM")
    plt.legend()
    plt.grid(True)
    plt.show()
