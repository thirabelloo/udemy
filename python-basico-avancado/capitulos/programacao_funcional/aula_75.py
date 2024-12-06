"""Exercícios com funções """

# """Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável."""


def multiplicador_numeros(*args):
    """
    Calcula o produto de uma quantidade variável de números e retorna o resultado como uma string.

    Parâmetros:
    *args (int ou float): Uma quantidade variável de números a serem multiplicados.

    Retorna:
    str: Uma string informando o resultado da multiplicação dos números fornecidos.
    """
    multiplicador = 1
    for numero in args:
        multiplicador *= numero
    return f"O valor da multiplicacao é: {multiplicador}"


MULTIPLICACAO = multiplicador_numeros(10, 2, 3, 4, 5)
print(MULTIPLICACAO)

# """Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar."""


def verifica_par_ou_impar(numero):
    """
    Verifica se um número é par ou ímpar e imprime o resultado.

    Parâmetros:
    numero (int): O número a ser verificado.

    Retorna:
    None
    """
    if numero % 2 == 0:
        print(f"O número: {numero} é par")
    else:
        print(f"O número: {numero} é ímpar")


verifica_par_ou_impar(2)
verifica_par_ou_impar(3)
verifica_par_ou_impar(15)
verifica_par_ou_impar(16)

outro_par_impar = verifica_par_ou_impar
# DOIS_E_PAR = outro_par_impar(2)
# print(DOIS_E_PAR)
print(verifica_par_ou_impar is outro_par_impar)
