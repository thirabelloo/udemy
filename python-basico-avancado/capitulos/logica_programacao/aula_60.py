"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

FRASE = "   Olha só que   , coisa interessante          "
# print(frase)
lista_frases_cruas = FRASE.split(",")
# print(lista_frases_cruas)

lista_frases = [frase.strip() for frase in lista_frases_cruas]

print(lista_frases_cruas)
print(lista_frases)


FRASES_UNIDAS = ", ".join(lista_frases)
print(FRASES_UNIDAS)
