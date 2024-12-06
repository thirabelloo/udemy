"""Exercícios"""

# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def duplicar_valor(numero):
    """
    Retorna o valor do número fornecido multiplicado por dois.

    Parâmetros:
    numero (int ou float): O número a ser duplicado.

    Retorna:
    int ou float: O resultado do número multiplicado por dois.
    """
    return numero * 2


def triplar_valor(numero):
    """
    Retorna o valor do número fornecido multiplicado por três.

    Parâmetros:
    numero (int ou float): O número a ser triplicado.

    Retorna:
    int ou float: O resultado do número multiplicado por três.
    """
    return numero * 3


def quadruplicar_valor(numero):
    """Retorna o valor do número fornecido multiplicado por quatro.

    Parâmetros:
    numero (int ou float): O número a ser quadruplicado.

    Retorna:
    int ou float: O resultado do número multiplicado por quatro.
    """
    return numero * 4


print(duplicar_valor(2))
print(triplar_valor(2))
print(quadruplicar_valor(2))

# Uma forma mais agil e inteligente de resolver o exercicio


def criar_multiplicador(multiplicador):
    """Cria uma função que multiplica um número pelo multiplicador fornecido.

    Parâmetros:
    multiplicador (int ou float): O valor pelo qual os números serão multiplicados.

    Retorna:
    function: Uma função que aceita um número e retorna o resultado da multiplicação desse número pelo multiplicador.
    """

    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_multiplicador(2)
triplar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplar(2))
print(quadruplicar(2))
