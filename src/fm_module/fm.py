import numpy as np

def fm_modulate(baseband_frequency, baseband_amplitude, modulation_frequency, modulation_index=0.5, t=None):
    if t is None:
        t = np.linspace(0, 1, 1000, endpoint=False)
    return baseband_amplitude * np.sin(2 * np.pi * baseband_frequency * t + modulation_index * np.sin(2 * np.pi * modulation_frequency * t))


