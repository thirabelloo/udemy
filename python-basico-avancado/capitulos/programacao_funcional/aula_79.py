"""Manipulando chaves e valores em dicionarios"""

pessoa = {
    "nome": "Thiago Rabello",
    "sobrenome": "Santos",
    "idade": 20,
    "altura": 1.8,
    "enderecos": [
        {"rua": "tal tal", "numero": 123},
        {"rua": "outra rua", "numero": 321},
    ],
}

print(pessoa)
print(pessoa["nome"])
print(pessoa["sobrenome"])
print(pessoa["idade"])
print(pessoa["enderecos"])
print(pessoa["enderecos"][0])
print(pessoa["enderecos"][1])
