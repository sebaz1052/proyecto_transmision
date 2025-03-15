from mpsk_module.mpsk import mpsk
from digital_input_module.digital_input import text_to_signal
from analog_input_module.analog_input import anolog_input_wav
from pcm_module.pcm import pcm
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # times, values = anolog_input_wav('./a2.wav', begin=0, end= 20000)
    # plt.plot(times, values)
    # plt.xlabel('Tiempo (s)')
    # plt.ylabel('Amplitud')
    # plt.title('Segmento de audio')
    # plt.show()
    
    # print(times, values)
    # print(len(times), len(values))
    vals = [-5, 0, 3 , 4, 5, 2, -1, -2 , 4, 0, 2, -4, 2, 5]
    print( pcm(vals, 16) )
    # t, signal, sample_times, sample_values = text_to_signal("T")
    # M = 2
    # signal, t_total = mpsk(sample_values, M )

    # plt.figure(figsize=(10, 4))
    # plt.plot(t_total, signal, label="Señal modulada (MPSK)")
    # plt.xlabel("Tiempo (s)")
    # plt.ylabel("Amplitud")
    # plt.title(f"Señal {M}-PSK modulada en fase")
    # plt.legend()
    # plt.grid()
    # plt.show()
    