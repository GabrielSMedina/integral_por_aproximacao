from utils import funcao
import numpy as np
import matplotlib.pyplot as plt


def retangulo_integral(x0, x1, num_iteracoes, graficos):
    base = (x1 - x0) / num_iteracoes

    integral_aproximada = 0
    for iteracao in range(1, num_iteracoes + 1):
        area = funcao(base * iteracao + x0) * base
        integral_aproximada += abs(area)

    if graficos:
        plotar_retangulo(x0, x1, num_iteracoes)

    return integral_aproximada


def plotar_retangulo(x0, x1, num_iteracoes):
    # Dados da reta
    x_curva = np.linspace(x0, x1, 100)  # Cria 100 pontos no intervalo de 0 a 6
    y_curva = funcao(x_curva)

    # Dados de formação dos retângulos
    x_retangulo = np.linspace(x0, x1, num_iteracoes + 1)
    y_retangulo = funcao(x_retangulo)

    for i in range(num_iteracoes):
        xi = [x_retangulo[i], x_retangulo[i + 1], x_retangulo[i + 1], x_retangulo[i]]
        yi = [0, 0, y_retangulo[i + 1], y_retangulo[i + 1]]
        plt.fill(xi, yi, color='green', alpha=0.4)

    plt.plot(x_curva, y_curva, color='black')

    # Adicionando rótulos aos eixos
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    # Adicionando um título ao gráfico
    plt.title(f'Gráfico de retângulos', fontsize=16)

    # Exibindo o gráfico
    plt.show()