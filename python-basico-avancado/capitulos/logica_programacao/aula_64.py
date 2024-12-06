"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

A = 10
B = 11

CONDICAO = A == B
print(CONDICAO)

VARIAVEL = "Valor" if CONDICAO else "Outro valor"
print(VARIAVEL)

DIGITO = 9
NOVO_DIGITO = DIGITO if DIGITO <= 9 else 0
print(NOVO_DIGITO)

NOVO_DIGITO = 0 if DIGITO > 9 else DIGITO
print(NOVO_DIGITO)

# COND_1 = False
# COND_2 = False
# print("Valor" if COND_1 else "Outro valor" if COND_2 else "Fim")
