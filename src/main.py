from digital_input_module.digital_input import text_to_signal
from am_module.am import am_modulate
from ask_module.ask import ask_modulate
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    text = "Hello World"
    # Generar la señal digital (moduladora) a partir del texto
    t, digital_signal, sample_times, sample_vals = text_to_signal(text)

    # Parametros comunes
    carrier_freq = 100  # Frecuencia de la portadora en Hz
    # Genera la señal portadora
    carrier = np.cos(2*np.pi*carrier_freq*t)

    # Bloque para modulacion ASK (on-off keying)
    a1 = 1.0  # Amplitud para bit '1'; para bit '0' se transmite 0
    modulated_signal = ask_modulate(digital_signal, t, carrier_freq, a1)

    # Bloque para modulacion AM
    # bias = 0.5  # Desplazamiento para asegurar que la envolvente sea positiva
    # modulation_index = 0.5  # Factor de modulacion que escala la señal base
    # modulated_signal = am_modulate(
    #    digital_signal, t, carrier_freq, bias, modulation_index)

    # Construccion de la grafica
    fig, axs = plt.subplots(3, 1, figsize=(10, 4), sharex=True)

    # Señal moduladora
    axs[0].plot(t, digital_signal,
                label="Señal moduladora (Digital)", color="blue")
    axs[0].set_title("Señal moduladora (Digital)")
    axs[0].set_ylabel("Amplitud")
    axs[0].legend()
    axs[0].grid(True)

    # Señal portadora
    axs[1].plot(t, carrier, label="Señal portadora", color="orange")
    axs[1].set_title("Señal portadora")
    axs[1].set_ylabel("Amplitud")
    axs[1].legend()
    axs[1].grid(True)

    # Señal modulada (ASK o AM)
    axs[2].plot(t, modulated_signal, label="Señal modulada", color="green")
    axs[2].set_title("Señal modulada")
    axs[2].set_xlabel("Tiempo (s)")
    axs[2].set_ylabel("Amplitud")
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()
