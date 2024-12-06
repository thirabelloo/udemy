"""Métodos úteis dos dicionários em Python
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro"""

pessoa = {"Nome": "Thiago", "Sobrenome": "Rabello", "Idade": 30}

print(pessoa.get("Nome", "None"))
# nome_pop = pessoa.pop('Nome')
# print(nome_pop, pessoa)

# nome_popitem = pessoa.popitem()
# print(nome_popitem, pessoa)

pessoa.update({"Nome": "Eduardo", "Sobrenome": "Carlos", "Cidade": "SP"})

pessoa.update(nome="Lucas", sobrenome="Brasil", idade=30, cidade="Parana")
print(pessoa)
