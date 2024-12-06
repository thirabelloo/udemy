"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    """
    Imprime os valores dos parâmetros e a soma dos três números fornecidos.

    Parâmetros:
    x (int ou float): O primeiro número.
    y (int ou float): O segundo número.
    z (int ou float): O terceiro número.

    Retorna:
    None
    """
    # Definição
    print(f"{x=} y={y} {z=}" " |", "x + y + z =", x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep="-")
