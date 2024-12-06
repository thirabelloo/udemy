"""
Desempacotamento em chamadas de métodos e funções
"""

STRING = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"
salas = [["Maria", "Helena"], ["Elaine"], ["Luiz", "João", "Eduarda"]]


p, b, *_, ap, u = lista
print(p, u, ap)

print("**************************\n")

# for nome in lista:
#     print(nome, end=" ")

# print("**************************\n")

print("Maria", "Helena", 1, 2, 3, "Eduarda")
print(*lista)
print(*STRING)
print(*tupla)
print(*salas, sep="\n")
