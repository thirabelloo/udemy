""" while/else """

STRING = "Valor qualquer"

i = 0
while i < len(STRING):
    LETRA = STRING[i]

    if LETRA == " ":
        break

    print(LETRA)
    i += 1
else:
    print("Não encontrei um espaço na string.")
print("Fora do while.")
