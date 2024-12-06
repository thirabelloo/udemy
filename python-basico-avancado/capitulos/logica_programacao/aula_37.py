"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

CONTADOR = 0

while CONTADOR <= 100:
    CONTADOR += 1

    if CONTADOR == 6:
        print("Não vou mostrar o 6.")
        continue

    if 10 <= CONTADOR <= 27:
        print("Não vou mostrar o", CONTADOR)
        continue

    print(CONTADOR)

    if CONTADOR == 40:
        break


print("Acabou")
