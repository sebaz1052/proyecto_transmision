import numpy as np
def pcm(values, M):

    min_valor = np.min(values)
    max_valor = np.max(values)

    # Dividir el intervalo en M niveles
    levels = np.linspace(min_valor, max_valor, M)
    for i in range(len(levels)):
        print( str(i) + " " + str(levels[i]))

    # Aproximar cada muestra al nivel más cercano
    valores_pcm = np.array([np.argmin(np.abs(levels - v)) for v in values])
    # valores_pcm = np.array([levels[np.argmin(np.abs(levels - v))] for v in values])

    return valores_pcm