"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

NUMERO_1 = 0.1
NUMERO_2 = 0.7
NUMERO_3 = NUMERO_1 + NUMERO_2
print(NUMERO_3)
print(f"{NUMERO_3:.2f}")
print(round(NUMERO_3, 2))

print("*****************************************")

numero_decimal_1 = decimal.Decimal("0.1")
numero_decimal_2 = decimal.Decimal("0.7")
numero_decimal_3 = numero_decimal_1 + numero_decimal_2
print(numero_decimal_3)
print(f"{numero_decimal_3:.2f}")
print(round(numero_decimal_3, 2))
