# Constantes para cores
cor_fill = 'purple'
cor_curva = 'black'


def funcao(x):
    return x**2
    # return -(x ** 3) + ((3*x)**2) - (17*x) + 3
    # return -(x ** 2) + (x * 3) - 2


def rodar_testes(x0, x1, iteracoes, graficos, teste):

    if teste == 1:
        teste_unico(x0, x1, iteracoes, graficos)
    else:
        teste_incremental(x0, x1, iteracoes, graficos)


def teste_unico(x0, x1, iteracoes, graficos):

    from met_monte_carlo import monte_carlo_integral
    from met_retangulos import retangulo_integral
    from met_trapezios import trapezio_integral
    from met_simpson import metodo_simpson

    print(
        f'número de iterações: {iteracoes}\n'
        f'Integral por monte carlos(abs A): {monte_carlo_integral(x0, x1, iteracoes, graficos):.4f}\n'
        f'Integral por Retângulos(abs A): {retangulo_integral(x0, x1, iteracoes, graficos):.4f}\n'
        f'Integral por Trapézio(abs A): {trapezio_integral(x0, x1, iteracoes, graficos):.4f}\n'
        f'Integral por Simpson: {metodo_simpson(x0, x1, iteracoes, graficos):.4f}\n'
    )


def teste_incremental(x0, x1, iteracoes, graficos):

    from met_monte_carlo import monte_carlo_integral
    from met_retangulos import retangulo_integral
    from met_trapezios import trapezio_integral
    from met_simpson import metodo_simpson
    # Bloco de incrementação de iterações
    while iteracoes <= 10000:
        print(
            f'número de iterações: {iteracoes}\n'
            f'Integral por monte carlos: {monte_carlo_integral(x0, x1, iteracoes, graficos):.4f}\n'
            f'Integral por Retângulos: {retangulo_integral(x0, x1, iteracoes, graficos):.4f}\n'
            f'Integral por Trapézio: {trapezio_integral(x0, x1, iteracoes, graficos):.4f}\n'
            f'Integral por Simpson: {metodo_simpson(x0, x1, iteracoes, graficos):.4f}'
        )
        print('_' * 100)
        iteracoes *= 10
