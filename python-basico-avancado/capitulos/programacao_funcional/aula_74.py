"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-se de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    """
    Calcula a soma de uma quantidade variável de números.

    Parâmetros:
    *args (int ou float): Uma quantidade variável de números a serem somados.

    Retorna:
    int ou float: A soma de todos os números fornecidos como argumentos.
    """
    total = 0
    for numero in args:
        total += numero
    return total


SOMA_1_2_3 = soma(1, 2, 3)
print(SOMA_1_2_3)

SOMA_4_5_6 = soma(4, 5, 6)
print(SOMA_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
OUTRA_SOMA = soma(*numeros)
print(OUTRA_SOMA)

print(sum(numeros))
print(*numeros)
