"""Métodos úteis dos dicionários em Python
copy - retorna uma cópia rasa (shallow copy)
"""

import copy

pessoa = {"Nome": "Thiago", "Sobrenome": "Rabello", "Idade": 30, "Lista": [0, 1, 2]}

pessoa_copy = copy.deepcopy(pessoa)
pessoa_copy["Idade"] = 25
pessoa_copy["Lista"][1] = 99

print(pessoa)
print(pessoa_copy)
