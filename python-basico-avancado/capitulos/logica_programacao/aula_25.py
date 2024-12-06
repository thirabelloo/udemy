"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

NOME = "Thiago"
PRECO = 1000.95897643
VARIAVEL = f"{NOME}, o preço é R${PRECO:.2f}"
NUMERO = 1500
print(VARIAVEL)
print(f"O hexadecimal de {NUMERO} é {NUMERO:08X}")
