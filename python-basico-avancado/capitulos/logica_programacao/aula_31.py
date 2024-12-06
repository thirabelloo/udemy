"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

CONDICAO = False
PASSOU_NO_IF = None

if CONDICAO:
    PASSOU_NO_IF = True
    print("Faça algo")
else:
    print("Não faça algo")


if PASSOU_NO_IF is None:
    print("Não passou no if")
else:
    print("Passou no if")
