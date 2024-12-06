"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(mensagem, nome):
    """Retorna uma mensagem de saudação personalizada.

    Parâmetros:
    mensagem (str): A mensagem de saudação.
    nome (str): O nome da pessoa a ser saudada.

    Retorna:
    str: Uma mensagem de saudação formatada com o nome.
    """
    return f"{mensagem}, {nome}!"


def executa(funcao, *args):
    """
    Executa uma função com argumentos fornecidos.

    Parâmetros:
    funcao (function): A função a ser executada.
    *args (tuple): Argumentos a serem passados para a função.

    Retorna:
    qualquer tipo: O resultado da execução da função com os argumentos fornecidos.
    """
    return funcao(*args)


print(executa(saudacao, "Bom dia", "Thiago"))
print(executa(saudacao, "Boa noite", "Maria"))
