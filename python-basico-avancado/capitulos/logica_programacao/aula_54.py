"""
Exercício
Exiba os índices da lista
0 Maria
1 Paulo
2 Juca
"""

lista = ["Maria", "Paulo", "Juca"]
lista.append("Thiago")

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

print("*******************************************************")

for indice, nome in enumerate(lista):
    print(indice, nome, type(nome))
