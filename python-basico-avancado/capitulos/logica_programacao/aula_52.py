"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ["Thiago", "Maria", 1, True, 1.1]
lista_b = lista_a.copy()

lista_a[0] = "Neymar"
print(lista_a)
print(lista_b)
