import numpy as np
from matplotlib import pyplot as plt
import utils
from utils import funcao


def metodo_simpson(x0, x1, num_sub_intervalos, grafico):

    num_iteracoes = validar_iteracoes(num_sub_intervalos)

    len_intervalo = (x1 - x0) / num_iteracoes

    soma = funcao(x0) + funcao(x1)  # Soma dos pontos min & max

    for valor in range(1, num_iteracoes):
        x = x0 + valor * len_intervalo
        if valor % 2 == 0:
            soma += 2 * funcao(x)
        else:
            soma += 4 * funcao(x)

    if grafico:  # se parâmetro graficos for TRUE, plotar gráficos
        plotar_simpson(x0, x1, num_iteracoes)

    integral_aproximada = abs(len_intervalo / 3 * soma)
    return integral_aproximada


def plotar_simpson(x0, x1, num_iteracoes):

    x_vals = np.linspace(x0, x1, 100)  # Cria 100 pontos no intervalo [x0, x1]
    y_vals = funcao(x_vals)  # Cria 100 pontos no intervalo [y0, y1]

    # Plotando a função
    plt.plot(x_vals, y_vals, color=utils.cor_curva)

    # Preenchendo os intervalos
    x_fill = np.linspace(x0, x1, num_iteracoes + 1)
    y_fill = funcao(x_fill)
    plt.fill_between(x_fill, y_fill, alpha=0.4, color=utils.cor_fill)

    # Adicionando um título ao gráfico
    plt.title(f'Gráfico de Simpson: {num_iteracoes} Iterações', fontsize=16)

    # Adicionando rótulos aos eixos
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    # Exibindo o gráfico
    plt.show()


def validar_iteracoes(num_iteracoes):  # Função destinada a garantir que o numero de iterações seja par

    if num_iteracoes % 2 != 0:
        return num_iteracoes + 1
    return num_iteracoes
