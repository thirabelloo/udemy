"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(a, b, c):
#     print("Várias1")
#     print("Várias2")
#     print("Várias3")
#     print("Várias4")


def imprimir(a, b, c):
    """
    Imprime três valores fornecidos como parâmetros.

    Parâmetros:
    a (qualquer tipo): O primeiro valor a ser impresso.
    b (qualquer tipo): O segundo valor a ser impresso.
    c (qualquer tipo): O terceiro valor a ser impresso.

    Retorna:
    None
    """
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)


def saudacao(nome="Sem nome"):
    """
    Imprime uma mensagem de saudação com o nome fornecido.

    Parâmetros:
    nome (str): O nome da pessoa a ser saudada.
    O padrão é "Sem nome" se nenhum nome for fornecido.

    Retorna:
    None
    """
    print(f"Olá, {nome}!")


saudacao("Thiago Rabello")
saudacao("Maria")
saudacao("Helena")
saudacao()
