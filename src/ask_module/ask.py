import numpy as np
import matplotlib.pyplot as plt


def ask_modulate(baseband_signal, t, carrier_freq=100, a1=1.0):
    """
    Aplica modulación por desplazamiento de amplitud (ASK) a la señal digital baseband.

    Parámetros:
      - baseband_signal: Vector de la señal digital (niveles 0 y 1).
      - t: Vector de tiempo (debe tener la misma longitud que baseband_signal).
      - carrier_freq: Frecuencia de la portadora en Hz.
      - A1: Amplitud cuando el bit es '1'. Para un bit '0' se transmite 0.

    Retorna:
      - modulated_signal: Señal ASK resultante.
    """
    # Generar la portadora sinusoidal
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    # Para ASK binaria (on-off keying):
    # Si el bit es 1 (o mayor que 0.5), se transmite la portadora a amplitud A1;
    # Si es 0, se transmite 0.
    modulated_signal = np.where(baseband_signal > 0.5, a1 * carrier, 0.0)
    return modulated_signal


def ask_modulate_analog(analog_signal, t, carrier_freq=100, a1=1.0, threshold=0.0):
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    modulated_signal = np.where(analog_signal > threshold, a1 * carrier, 0.0)
    return modulated_signal


if __name__ == '__main__':
    # Ejemplo: Usar una señal digital simple (onda cuadrada) generada manualmente.
    fs = 1000  # Frecuencia de muestreo
    t = np.linspace(0, 1, fs, endpoint=False)
    # Señal digital: bits alternados (0 y 1)
    baseband = np.where((t * 10 % 1) < 0.5, 0, 1)

    mod_signal = ask_modulate(baseband, t, carrier_freq=100, a1=1.0)

    plt.figure(figsize=(10, 4))
    plt.plot(t, mod_signal, label="Señal ASK")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Ejemplo de modulación ASK")
    plt.legend()
    plt.grid(True)
    plt.show()
