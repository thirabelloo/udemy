"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ["Maria", "Helena", "Liz"]
nome_1, nome_2, nome_3 = nomes
# nome_1, nome_2, nome_3 = ['Maria', 'Helena', 'Liz']
print(nome_1)
print(nome_2)
print(nome_3)

print("***************************")

# lista_nomes = ["Fabio", "Hugo", "Thiago"]
_, __, nome, *resto = ["Fabio", "Hugo", "Thiago"]
print(_)
print(__)
print(nome)
print(resto)
