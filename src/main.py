from fm_module.fm import fm_modulate
from fsk_module.fsk import fsk_modulate

def main():
    # Ejecutar la modulación FM
    print("Ejecutando modulación FM...")
    fm_modulate('AudioPrueba.wav')

    # Ejecutar la modulación FSK
    print("Ejecutando modulación FSK...")
    text = "H"
    fsk_modulate(text)

if __name__ == '__main__':
    main()