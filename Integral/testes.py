import matplotlib.pyplot as plt
import numpy as np


def teste1():
    t = np.linspace(0, 2 * np.pi, 1000)

    y1 = np.cos(4 * t)
    y2 = np.sin(4 * t)

    plt.figure('Cosseno', figsize=(5, 4))
    plt.plot(t, y1, color='purple', linewidth=1)
    plt.title("Cosseno")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")

    plt.figure('Seno')
    plt.plot(t, y2, color='purple', linewidth=1)
    plt.title("Seno")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")

    plt.show()


def teste2():
    t = np.linspace(0, np.pi*2, 100)
    y1 = np.cos(t)
    y2 = np.sin(t)

    plt.figure('Grafico')
    plt.plot(t, y1)
    plt.plot(t, y2)
    plt.grid()
    plt.title('Grafico de seno e cosseno', fontsize=16)
    plt.xlabel('Tempo (s)', fontsize=14)
    plt.ylabel('Amplitude', fontsize=14)
    plt.show()


def teste3():
    x = np.linspace(0, 2*np.pi, 500)
    cos = np.cos(x)
    sen = np.sin(x)

    plt.figure('Grafico', figsize=(7, 8))
    plt.subplots_adjust(
        wspace=0.450,
        hspace=0.450
    )

    plt.subplot(2, 1, 1)
    plt.plot(x, cos, color='purple')
    plt.xlabel('tempo', fontsize=14)
    plt.ylabel ('Amplitude', fontsize=14)
    plt.title('Cosseno', fontsize=16)
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(x, sen, color='purple')
    plt.xlabel('tempo', fontsize=14)
    plt.ylabel('Amplitude', fontsize=14)
    plt.title('Seno', fontsize=16)
    plt.grid()

    plt.show()


teste3()