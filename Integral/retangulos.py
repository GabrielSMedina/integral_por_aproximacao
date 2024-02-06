import matplotlib.pyplot as plt
import numpy as np

def funcao(x):
    return (-x)**3  # Altere a função conforme necessário

def metodo_retangulos(funcao, intervalo, num_iteracoes):
    a, b = intervalo
    h = (b - a) / num_iteracoes

    x = np.linspace(a, b, num_iteracoes + 1)
    y = funcao(x)

    plt.plot(x, y, color='blue', linewidth=2, label='(-x)**3')

    for i in range(num_iteracoes):
        xi = [x[i], x[i+1], x[i+1], x[i], x[i]]
        yi = [0, 0, y[i+1], y[i+1], 0]
        plt.fill(xi, yi, color='gray', alpha=0.5)

    plt.title('Método de Retângulos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Exemplo de uso:
intervalo = (-5, 5)
num_iteracoes = 35

metodo_retangulos(funcao, intervalo, num_iteracoes)
