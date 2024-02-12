import utils
from utils import funcao
import numpy as np
import matplotlib.pyplot as plt


def trapezio_integral(x0, x1, num_iteracoes, graficos):
    base_intervalo = (x1 - x0) / num_iteracoes  # Calculo da base do intervalo

    integral_aproximada = 0.5 * abs((funcao(x0) + funcao(x1)))  # Calculo da média da altura
    for i in range(1, num_iteracoes):
        area = x0 + i * base_intervalo
        integral_aproximada += abs(funcao(area))

    if graficos:  # se parâmetro graficos for TRUE, plotar gráficos
        plotar_trapezio(x0, x1, num_iteracoes)

    integral_aproximada *= base_intervalo
    return integral_aproximada


def plotar_trapezio(x0, x1, num_iteracoes):
    # Dados da reta
    x_curva = np.linspace(x0, x1, 100)  # Cria 100 pontos no intervalo de 0 a 6
    y_curva = funcao(x_curva)

    x = np.linspace(x0, x1, num_iteracoes + 1)
    y = funcao(x)

    # Plotando a função
    plt.plot(x_curva, y_curva, color=utils.cor_curva, alpha=0.6)

    for i in range(num_iteracoes):
        xi = [x[i], x[i + 1]]
        yi = [y[i], y[i + 1]]
        plt.fill_between(xi, yi, color=utils.cor_fill, alpha=0.4)

    # Adicionando um título ao gráfico
    plt.title(f'Gráfico trapézios: {num_iteracoes} Iterações', fontsize=16)

    # Adicionando rótulos aos eixos
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    # Exibindo o gráfico
    plt.show()
