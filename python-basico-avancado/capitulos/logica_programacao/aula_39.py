"""
Iterando strings com while
"""

NOME = "Thiago Rabello"  # Iteráveis
# print(NOME[-14])


NOME = "Thiago Rabello"  # Iteráveis

INDICE = 0
NOVO_NOME = ""
while INDICE < len(NOME):
    LETRA = NOME[INDICE]
    NOVO_NOME += f"*{LETRA}"
    INDICE += 1

NOVO_NOME += "*"
print(NOVO_NOME)
