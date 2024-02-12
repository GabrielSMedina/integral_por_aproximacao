def funcao(x):
    #return x**2
    #return -(x ** 3) + ((3*x)**2) - (17*x) + 3
    return -(x**2)+(x*3)-2


def rodar_testes(x0, x1, iteracoes, graficos):
    from met_carlo import monte_carlo_integral
    from met_retangulos import retangulo_integral
    from met_trapezios import trapezio_integral

    print(f'Integral por monte carlos: {monte_carlo_integral(x0, x1, iteracoes, graficos):.4f}, com {iteracoes} iterações')
    print(f'Integral por Retângulos: {retangulo_integral(x0, x1, iteracoes, graficos):.4f}, com {iteracoes} iterações')
    print(f'Integral por Trapézio: {trapezio_integral(x0, x1, iteracoes, graficos):.4f}, com {iteracoes} iterações')
    '''
    # Bloco de incrementação de iterações
    while iteracoes <= 10000:
        print(f'Integral por monte carlos: {monte_carlo_integral(x0, x1, iteracoes, graficos):.4f}, com {iteracoes} pontos')
        print(f'Integral por Retângulos: {retangulo_integral(x0, x1, iteracoes, graficos):.4f}, com {iteracoes} pontos')
        print(f'Integral por Trapézio: {trapezio_integral(x0, x1, iteracoes, graficos):.4f}, com {iteracoes} pontos')
        print('_' * 100)
        iteracoes *= 10
    '''
