import numpy as np
import matplotlib.pyplot as plt
from utils import funcao


def monte_carlo_integral(x0, x1, num_iteracoes, graficos):
    x = np.random.uniform(x0, x1, num_iteracoes)

    # Gere y no intervalo entre o mínimo e máximo da função
    y_min = min(funcao(x))
    y_max = max(funcao(x))
    y = np.random.uniform(y_min, y_max, num_iteracoes)

    # pontos_abaixo = np.sum(y < funcao(x))
    pontos_abaixo = calcula_pontos(x, y, num_iteracoes)

    area_retangulo = abs((x1 - x0)) * (y_max - y_min)

    aproximacao_integral: float = (pontos_abaixo / num_iteracoes) * area_retangulo

    if graficos:
        plotar_monte_carlo(x, y, x0, x1, num_iteracoes)

    return aproximacao_integral


def plotar_monte_carlo(x, y, x0, x1, num_iteracoes):
    # Dados da reta
    x_curva = np.linspace(x0, x1, 100)  # Cria 100 pontos no intervalo [x0, x1]
    y_curva = funcao(x_curva)

    # Plotando os pontos
    plt.scatter(x, y, color='green', marker='o', alpha=0.6)

    # Plotando a curva x**2
    plt.plot(x_curva, y_curva, color='black')

    # Adicionando rótulos aos eixos
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    # Adicionando um título ao gráfico
    plt.title(f'Gráfico de pontos gerados: {num_iteracoes} Iterações', fontsize=16)

    # Exibindo o gráfico
    plt.show()


def calcula_pontos(x, y, num_iteracoes):
    pontos = 0
    for valor in range(0, num_iteracoes):
        if y[valor] >= 0:
            if y[valor] < funcao(x[valor]):
                pontos += 1
        else:
            if y[valor] > funcao(x[valor]):
                pontos += 1

    return pontos
