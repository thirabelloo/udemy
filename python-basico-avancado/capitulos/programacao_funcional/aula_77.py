"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    """
    Cria uma função de saudação personalizada com uma saudação específica.

    Parâmetros:
    saudacao (str): A saudação a ser usada na mensagem.

    Retorna:
    function: Uma função que aceita um nome e retorna uma mensagem de saudação personalizada.
    """

    def saudar(nome):
        """
        Retorna uma mensagem de saudação personalizada com o nome fornecido.

        Parâmetros:
        nome (str): O nome da pessoa a ser saudada.

        Retorna:
        str: Uma mensagem de saudação personalizada.
        """
        return f"{saudacao}, {nome}"

    return saudar


falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

for pessoa in ["Maria", "Joana", "Lucas"]:
    print(falar_bom_dia(pessoa))
    print(falar_boa_noite(pessoa))
