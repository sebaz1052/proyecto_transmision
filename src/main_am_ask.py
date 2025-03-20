from digital_input_module.digital_input import text_to_signal
from analog_input_module.analog_input import anolog_input_wav
from am_module.am import am_modulate, am_modulate_analog
from ask_module.ask import ask_modulate, ask_modulate_analog
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # -----------------------------------------------------
    # Selección de la fuente de la señal moduladora:
    # 'digital' => a partir de texto (señal digital: 0/1)
    # 'analog'  => a partir de un archivo WAV (señal analógica)
    source_type = 'analog'

    # -----------------------------------------------------
    # Parámetros comunes
    carrier_freq = 100  # Frecuencia de la portadora en Hz

    if source_type == 'digital':
        # Para la fuente digital se utiliza la función que convierte texto en señal digital
        text = "Hello World"
        t, baseband_signal, sample_times, sample_vals = text_to_signal(text)
    else:
        # Para la fuente analógica se lee un archivo WAV
        # Reemplaza 'ruta_del_audio.wav' con la ruta real a tu archivo WAV
        file = './AudioPrueba.wav'
        t, baseband_signal = anolog_input_wav(file, start_time=0, end_time=2)

    # Generar la señal portadora
    carrier = np.cos(2 * np.pi * carrier_freq * t)

    # -----------------------------------------------------
    # Selección del tipo de modulación:
    # 'am'  => modulación en amplitud (AM)
    # 'ask' => modulación por desplazamiento de amplitud (ASK, on–off keying)
    modulation_type = 'ask'

    # -----------------------------------------------------
    # Aplicar la modulación según la fuente y el tipo seleccionado
    if source_type == 'digital':
        # Fuente digital: ya contamos con la señal binaria (0/1)
        if modulation_type == 'am':
            bias = 0.5             # Bias para asegurar envolvente positiva
            modulation_index = 0.5  # Factor que escala la señal base
            modulated_signal = am_modulate(
                baseband_signal, t, carrier_freq, bias, modulation_index)
        else:  # ASK
            a1 = 1.0  # Amplitud cuando el bit es '1'
            modulated_signal = ask_modulate(
                baseband_signal, t, carrier_freq, a1)
    else:
        # Fuente analógica: usamos la señal continua leída del archivo WAV
        if modulation_type == 'am':
            bias = 0.5
            modulation_index = 0.5
            # Función para modulación AM de señal analógica
            modulated_signal = am_modulate_analog(
                baseband_signal, t, carrier_freq, bias, modulation_index)
        else:
            a1 = 1.0
            threshold = 0.0  # Umbral para determinar si se "enciende" la portadora
            # Función para modulación ASK de señal analógica (convertida a on/off mediante umbral)
            modulated_signal = ask_modulate_analog(
                baseband_signal, t, carrier_freq, a1, threshold)

    # -----------------------------------------------------
    # Graficar las 3 señales: la señal moduladora, la portadora y la señal modulada
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    # 1. Señal moduladora (baseband)
    axs[0].plot(t, baseband_signal, label="Señal moduladora", color="blue")
    axs[0].set_title("Señal moduladora (Baseband)")
    axs[0].set_ylabel("Amplitud")
    axs[0].legend()
    axs[0].grid(True)

    # 2. Señal portadora
    axs[1].plot(t, carrier, label="Señal portadora", color="orange")
    axs[1].set_title("Señal portadora")
    axs[1].set_ylabel("Amplitud")
    axs[1].legend()
    axs[1].grid(True)

    # 3. Señal modulada (AM o ASK)
    axs[2].plot(t, modulated_signal,
                label=f"Señal modulada ({modulation_type.upper()})", color="green")
    axs[2].set_title(f"Señal modulada ({modulation_type.upper()})")
    axs[2].set_xlabel("Tiempo (s)")
    axs[2].set_ylabel("Amplitud")
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()
