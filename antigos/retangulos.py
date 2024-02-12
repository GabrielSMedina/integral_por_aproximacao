import matplotlib.pyplot as plt
import numpy as np

def funcao(x):
    return (x)**2  # Altere a função conforme necessário

def metodo_retangulos(funcao, intervalo, num_iteracoes):
    minimo, maximo = intervalo
    largura = (maximo - minimo) / num_iteracoes

    x_retangulo = np.linspace(minimo, maximo, num_iteracoes + 1)
    x_reta = np.linspace(minimo, maximo, 200)
    y_retangulo = funcao(x_retangulo)
    y_reta = funcao(x_reta)

    plt.plot(x_reta, y_reta, color='black', linewidth=1, label='x ^ 2')


    for i in range(num_iteracoes):
        xi = [x_retangulo[i], x_retangulo[i+1], x_retangulo[i+1], x_retangulo[i]]
        yi = [0, 0, y_retangulo[i+1], y_retangulo[i+1]]
        plt.fill(xi, yi, color='green', alpha=0.2)

    integral_aproximada = 0
    for iteracao in range(1, num_iteracoes):
        area = funcao(largura*iteracao) * largura
        integral_aproximada += area
    print(integral_aproximada)

    plt.title('Método de Retângulos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Exemplo de uso:
intervalo = (0, 15)
num_iteracoes = 500000

metodo_retangulos(funcao, intervalo, num_iteracoes)
