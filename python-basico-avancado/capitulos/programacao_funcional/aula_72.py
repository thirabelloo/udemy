"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz uma variável do escopo externo
ser a mesma no escopo interno.
"""

X = 1


def escopo():
    """
    Define uma variável local `x`, declara uma função aninhada e imprime valores dentro dela.

    A função `escopo` cria uma variável local `x` e declara a função aninhada `outra_funcao` que redefine `x`
    localmente e imprime `x` e `y`.

    Retorna:
    None
    """
    # global x
    x = 10

    def outra_funcao():
        """
        Redefine a variável `x` e define a variável `y`, depois imprime seus valores.

        Esta função aninhada redefine `x` para 11, define `y` como 2, e imprime ambos os valores.

        Retorna:
        None
        """
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(X)
escopo()
print(X)
