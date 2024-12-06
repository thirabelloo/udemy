"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

STRING = "1000"
OUTRA_VARIAVEL = f"{STRING[:3]}ABC{STRING[4:]}"
print(STRING)
print(OUTRA_VARIAVEL)
print(STRING.zfill(10))
