from mpsk_module.mpsk import mpsk
from digital_input_module.digital_input import text_to_signal
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("He")
    t, signal, sample_times, sample_values = text_to_signal("T")
    M = 2
    signal, t_total = mpsk(sample_values, M )

    plt.figure(figsize=(10, 4))
    plt.plot(t_total, signal, label="Señal modulada (MPSK)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title(f"Señal {M}-PSK modulada en fase")
    plt.legend()
    plt.grid()
    plt.show()
    