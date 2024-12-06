"""Contador de letras"""

FRASE = "thiago"

i = 0
QTD_APARECEU_MAIS_VEZES = 0
LETRA_APARECEU_MAIS_VEZES = ""

while i < len(FRASE):
    LETRA_ATUAL = FRASE[i]

    if LETRA_ATUAL == " ":
        i += 1
        continue

    QTD_ATUAL = FRASE.count(LETRA_ATUAL)

    if QTD_APARECEU_MAIS_VEZES <= QTD_ATUAL:
        QTD_APARECEU_MAIS_VEZES = QTD_ATUAL
        LETRA_APARECEU_MAIS_VEZES = LETRA_ATUAL

    i += 1

print(
    "A letra que apareceu mais vezes foi "
    f'"{LETRA_APARECEU_MAIS_VEZES}" que apareceu '
    f"{QTD_APARECEU_MAIS_VEZES}x"
)
