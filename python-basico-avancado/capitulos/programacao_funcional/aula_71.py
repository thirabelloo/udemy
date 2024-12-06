"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def soma(x, y, z=None):
    """
    Imprime os valores dos parâmetros e a soma dos números fornecidos.

    Parâmetros:
    x (int ou float): O primeiro número.
    y (int ou float): O segundo número.
    z (int ou float, opcional): O terceiro número, opcional.

    Retorna:
    None
    """
    if z is not None:
        print(f"{x=} {y=} {z=}", " |", "x + y + z =", x + y + z)
    else:
        print(f"{x=} {y=}", " |", "x + y =", x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
