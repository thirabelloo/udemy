"""Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro"""

pessoa = {"Nome": "Thiago", "Sobrenome": "Rabello", "Idade": 30}

print(len(pessoa))
print(pessoa.keys())
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
print(pessoa.setdefault("Idade", None))

print()
print(pessoa["Nome"])
print(pessoa.get("Nome", "Não existe"))

nome = pessoa.pop("Nome")
print()
print(nome)
print(pessoa)

ultima_chave = pessoa.popitem()
print()
print(ultima_chave)
print(pessoa)

pessoa.update(
    {
        "Nome": "Jiraya",
        "idade": 30,
    }
)
print()
print(pessoa)

pessoa.update(nome="Messi", idade=30)
print()
print(pessoa)

# tupla = (('Nome', 'Thomas'), ('Idade', 30))
lista = [["Nome", "Peter"], ["idade", 25]]
pessoa.update(lista)
print()
print(pessoa)
