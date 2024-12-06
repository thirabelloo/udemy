"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

QTD_LINHAS = 5
QTD_COLUNAS = 5

LINHA = 1
while LINHA <= QTD_LINHAS:
    COLUNA = 1
    while COLUNA <= QTD_COLUNAS:
        print(f"{LINHA=} {COLUNA=}")
        COLUNA += 1
    LINHA += 1


print("Acabou")
