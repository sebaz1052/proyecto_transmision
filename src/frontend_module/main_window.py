import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from src.digital_input_module.digital_input import text_to_signal
from src.analog_input_module.analog_input import anolog_input_wav
from src.am_module.am import am_modulate, am_modulate_analog
from src.ask_module.ask import ask_modulate, ask_modulate_analog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz de Modulación")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Panel de controles
        control_layout = QHBoxLayout()
        main_layout.addLayout(control_layout)

        # Selector de fuente de señal
        signal_label = QLabel("Tipo de Señal:")
        self.signal_combo = QComboBox()
        self.signal_combo.addItems(["Digital", "Analógica"])
        control_layout.addWidget(signal_label)
        control_layout.addWidget(self.signal_combo)

        # Selector de modulación
        modulation_label = QLabel("Modulación:")
        self.modulation_combo = QComboBox()
        # Puedes ampliar con más opciones
        self.modulation_combo.addItems(["AM", "ASK"])
        control_layout.addWidget(modulation_label)
        control_layout.addWidget(self.modulation_combo)

        # Botón para generar las gráficas
        self.generate_button = QPushButton("Generar Gráficas")
        self.generate_button.clicked.connect(self.generate_plots)
        control_layout.addWidget(self.generate_button)

        # Área de gráficas usando Matplotlib embebido
        self.figure = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

    def generate_plots(self):
        # Para este ejemplo generamos señales dummy.
        # En la versión final, reemplaza estos datos llamando a las funciones de tu proyecto.
        fs = 1000  # Frecuencia de muestreo
        # t = np.linspace(0, 1, fs, endpoint=False)
        carrier_freq = 100  # Frecuencia de la portadora en Hz

        # Según la fuente seleccionada: digital o analógica
        if self.signal_combo.currentText() == "Digital":
            # Señal digital
            # moduladora = np.where((t*10 % 1) < 0.5, 0, 1)
            text = "Hello World"
            t, baseband_signal, sample_times, sample_vals = text_to_signal(
                text)
        else:
            # Señal analógica
            # moduladora = 0.5 * (1 + np.sin(2 * np.pi * 3 * t))
            file = '../AudioPrueba.wav'
            t, baseband_signal = anolog_input_wav(
                file, start_time=0, end_time=2)

        # Generar la portadora
        carrier = np.cos(2 * np.pi * carrier_freq * t)

        # Según la modulación seleccionada: AM o ASK
        modulation_type = self.modulation_combo.currentText()
        if self.signal_combo.currentText() == "Digital":
            if modulation_type == "AM":
                bias = 0.5             # Bias para asegurar envolvente positiva
                modulation_index = 0.5  # Factor que escala la señal base
                modulated_signal = am_modulate(
                    baseband_signal, t, carrier_freq, bias, modulation_index)
            else:  # ASK
                a1 = 1.0  # Amplitud cuando el bit es '1'
                modulated_signal = ask_modulate(
                    baseband_signal, t, carrier_freq, a1)
        else:  # Fuente analógica
            if modulation_type == "AM":
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

        # Limpiar figura y crear tres subgráficas
        self.figure.clear()
        ax1 = self.figure.add_subplot(3, 1, 1)
        ax1.plot(t, baseband_signal, color='blue')
        ax1.set_title("Señal moduladora")
        ax1.grid(True)

        ax2 = self.figure.add_subplot(3, 1, 2)
        ax2.plot(t, carrier, color='orange')
        ax2.set_title("Señal portadora")
        ax2.grid(True)

        ax3 = self.figure.add_subplot(3, 1, 3)
        ax3.plot(t, modulated_signal, color='green')
        ax3.set_title(f"Señal modulada ({modulation_type})")
        ax3.set_xlabel("Tiempo (s)")
        ax3.grid(True)

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
