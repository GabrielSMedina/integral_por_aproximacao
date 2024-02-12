'''def integral_aproximada(funcao, intervalo, num_iteracoes):

    a, b = intervalo  # Limites inferior e superior do intervalo

    largura = (b - a) / num_iteracoes  # Largura de cada subintervalo

    integral_aproximada = 0
    for iteracao in range(1, num_iteracoes):
        area = funcao(largura*iteracao) * largura
        integral_aproximada += area

    return integral_aproximada


def integral_metodo_do_trapezio(funcao, intervalo, num_iteracoes):
    a, b = intervalo  # Limites inferior e superior do intervalo

    x = (b - a) / num_iteracoes  # Largura de cada subintervalo

    # Calcula a integral usando o método do trapézio
    integral_aproximada = 0.5 * (funcao(a) + funcao(b))
    for i in range(1, num_iteracoes):
        area = a + i * x
        integral_aproximada += funcao(area)

    integral_aproximada *= x
    return integral_aproximada

# Teste
def minha_funcao(x):
    return x**2

intervalo = (0, 10)

num_iteracoes = 10


print('A integral aproximada é: ', integral_aproximada(minha_funcao, intervalo, num_iteracoes))
print('A integral aproximada é por método do trapezio é: ', integral_metodo_do_trapezio(minha_funcao, intervalo, num_iteracoes))
'''