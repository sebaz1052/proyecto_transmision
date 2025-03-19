from digital_input_module.digital_input import text_to_signal
from am_module.am import am_modulate
from ask_module.ask import ask_modulate
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Procesar un texto de entrada para obtener la señal digital
    text = "Hello World"
    t, digital_signal, sample_times, sample_vals = text_to_signal(text)

    # Parámetros de modulación AM
    carrier_freq = 100      # Frecuencia de la portadora (Hz)
    bias = 0.5              # Bias para la envolvente
    modulation_index = 0.5  # Factor de modulación
    a1 = 1.0  # Amplitud para bit '1' (para bit '0' se transmite 0)

    # Aplicar modulación de amplitud usando la señal digital continua
    # signal = am_modulate(
    #    digital_signal, t, carrier_freq, bias, modulation_index)

    # Aplicar modulación por desplazamiento de amplitud
    signal = ask_modulate(digital_signal, t, carrier_freq, a1)

    # Graficar la señal modulada en AM
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal, label="Señal AM")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Señal modulada en AM a partir del texto: '{}'".format(text))
    plt.legend()
    plt.grid(True)
    plt.show()
