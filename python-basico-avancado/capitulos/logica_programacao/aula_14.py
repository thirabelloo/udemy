"""Utilizacao do format para formatacao de codigo"""

A = "AAAAA"
B = "BBBBBB"
C = 1.1
STRING = "b={nome2} a={nome1} a={nome1} c={nome3:.2f}"
FORMATO = STRING.format(nome1=A, nome2=B, nome3=C)

print(FORMATO)
