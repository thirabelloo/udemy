"""Calcula o valor de uma expressão matemática específica.
A expressão segue a ordem de precedência das operações"""

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
CONTA_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(CONTA_1)
