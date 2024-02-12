import numpy as np


def funcao(x):
    # Defina sua função aqui
    return x ** 2  # Exemplo de uma função quadrática


def monte_carlo_integral(a, b, n):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, max(funcao(x)), n)

    pontos_abaixo = np.sum(y < funcao(x))

    area_retangulo = (b - a) * max(funcao(x))

    aproximacao_integral = (pontos_abaixo / n) * area_retangulo

    return aproximacao_integral


# Exemplo de uso
a = 0
b = 1
n = 10000

resultado = monte_carlo_integral(a, b, n)
print(f"Aproximação da integral: {resultado}")
