"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    """
    Calcula a soma de dois números, retornando uma lista específica se o primeiro número for maior que 10.

    Parâmetros:
    x (int ou float): O primeiro número.
    y (int ou float): O segundo número.

    Retorna:
    int, float ou list: A soma dos dois números se `x` for menor ou igual a 10;
    caso contrário, uma lista contendo [10, 20].
    """
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
# print(variavel)

print(soma(2, 2))
print(soma(3, 3))
print(soma(11, 55))
