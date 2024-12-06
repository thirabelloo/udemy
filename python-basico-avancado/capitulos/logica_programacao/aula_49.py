"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis:
    append, insert, pop, del, clear, extend, +
Create Read Update  Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista = [
    10,
    20,
    30,
    40,
]
print(f"Lista original: {lista}")
lista[2] = 300
print(f"Item no indice [2]: {lista[2]}")
print(f"Modificadando um item da lista: {lista}")
del lista[2]
print(f"Lista apos deletar um item: {lista}")
print(f"Item no indice [2]: {lista[2]}")
print(f"Lista final: {lista}")
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
print(f"Adicionando e removendo valores na lista: {lista}")
