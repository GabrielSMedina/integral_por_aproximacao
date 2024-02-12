from utils import funcao
import numpy as np
import matplotlib.pyplot as plt


def trapezio_integral(x0, x1, num_iteracoes, graficos):
    base_intervalo = (x1 - x0) / num_iteracoes

    # Calcula a integral usando o método do trapézio
    integral_aproximada = 0.5 * abs((funcao(x0) + funcao(x1)))
    for i in range(1, num_iteracoes):
        area = x0 + i * base_intervalo
        integral_aproximada += abs(funcao(area))

    if graficos:
        plotar_trapezio(x0, x1, num_iteracoes)

    integral_aproximada *= base_intervalo
    return integral_aproximada


def plotar_trapezio(x0, x1, num_iteracoes):
    # Dados da reta
    x_curva = np.linspace(x0, x1, 100)  # Cria 100 pontos no intervalo de 0 a 6
    y_curva = funcao(x_curva)

    x = np.linspace(x0, x1, num_iteracoes + 1)
    y = funcao(x)

    plt.plot(x_curva, y_curva, color='black', alpha=0.6)

    for i in range(num_iteracoes):
        xi = [x[i], x[i + 1]]
        yi = [y[i], y[i + 1]]
        plt.fill_between(xi, yi, color='green', alpha=0.4)

    plt.title('Método do Trapézio')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
