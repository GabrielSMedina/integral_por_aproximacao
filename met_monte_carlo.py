import numpy as np
import matplotlib.pyplot as plt
import utils
from utils import funcao


def monte_carlo_integral(x0, x1, num_iteracoes, graficos):

    x = np.random.uniform(x0, x1, num_iteracoes)  # Gera numeros aleatórios para o eixo X

    # Gere y no intervalo entre o mínimo e máximo da função
    y_min = min(funcao(x))
    y_max = max(funcao(x))

    y = np.random.uniform(min(funcao(x)), max(funcao(x)), num_iteracoes)  # Gera numeros aleatórios para o eixo Y

    pontos_abaixo = calcula_pontos(x, y, num_iteracoes)  # Função para calcular pontos dentro da área da curva

    area_retangulo = abs((x1 - x0)) * (y_max - y_min)  # Calcula a área do retângulo que contem a curva A=Base x Altura

    aproximacao_integral: float = (pontos_abaixo / num_iteracoes) * area_retangulo  # (Pcurva/Ptotais)*Area_Retângulo

    if graficos:  # se parâmetro graficos for TRUE, plotar gráficos
        plotar_monte_carlo(x, y, x0, x1, num_iteracoes)

    return aproximacao_integral


def plotar_monte_carlo(x, y, x0, x1, num_iteracoes):
    # Dados da reta
    x_curva = np.linspace(x0, x1, 100)  # Cria 100 pontos no intervalo [x0, x1]
    y_curva = funcao(x_curva)  # Cria 100 pontos no intervalo [y0, y1]

    # Plotando os pontos
    plt.scatter(x, y, color=utils.cor_fill, marker='o', alpha=0.6)

    # Plotando a função
    plt.plot(x_curva, y_curva, color=utils.cor_curva)

    # Adicionando rótulos aos eixos
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    # Adicionando um título ao gráfico
    plt.title(f'Gráfico de pontos gerados: {num_iteracoes} Iterações', fontsize=16)

    # Exibindo o gráfico
    plt.show()


def calcula_pontos(x, y, num_iteracoes):  # Função destinada a calcular de forma distintas pontos positivos e negativos

    pontos = 0
    for valor in range(0, num_iteracoes):
        if 0 <= y[valor] < funcao(x[valor]):
            pontos += 1
        else:
            if y[valor] > funcao(x[valor]):
                pontos += 1

    return pontos
