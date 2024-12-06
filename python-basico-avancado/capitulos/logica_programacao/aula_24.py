"""Operadores in e not in"""

# Strings são iteráveis
#  0 1 2 3 4 5
#  T h i a g o
# -6-5-4-3-2-1
NOME = "Thiago"
print(NOME[2])
print(NOME[-4])
print("ago" in NOME)
print("zero" in NOME)
print(10 * "-")
print("ago" not in NOME)
print("zero" not in NOME)

NOME = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in NOME:
    print(f"{encontrar} está em {NOME}")
else:
    print(f"{encontrar} não está em {NOME}")
