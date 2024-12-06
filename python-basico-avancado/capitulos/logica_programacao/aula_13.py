"""Calculo de IMC de uma pessoa mais a formatacao f-strings"""

NOME = "Thiago Rabello"
ALTURA = 1.85
PESO = 80
IMC = PESO / ALTURA**2

"f-strings"
LINHA_1 = f"{NOME} tem {ALTURA:.2f} de altura,"
LINHA_2 = f"pesa {PESO} quilos e seu imc é"
LINHA_3 = f"{IMC:.2f}"

print(LINHA_1)
print(LINHA_2)
print(LINHA_3)
