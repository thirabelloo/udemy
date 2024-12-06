"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update  Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append("Thiago")
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista, nome)
