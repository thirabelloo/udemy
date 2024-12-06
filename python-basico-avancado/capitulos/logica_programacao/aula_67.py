"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
-  11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
-  77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

import re
import sys

CPF_ENVIADO_USUARIO_REPLACE = (
    "746.824.890-70".replace(".", "").replace(" ", "").replace("-", "")
)

print(CPF_ENVIADO_USUARIO_REPLACE)

entrada = input("CPF [746.824.890-70]: ")
cpf_enviado_usuario = re.sub(r"[^0-9]", "", entrada)

print(cpf_enviado_usuario)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print("Voce enviou dados sequenciais.")
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
CONTADOR_REGRESSIVO_1 = 10

RESULTADO_DIGITO_1 = 0
for digito in nove_digitos:
    RESULTADO_DIGITO_1 += int(digito) * CONTADOR_REGRESSIVO_1
    CONTADOR_REGRESSIVO_1 -= 1
digito_1 = (RESULTADO_DIGITO_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
CONTADOR_REGRESSIVO_2 = 11

RESULTADO_DIGITO_2 = 0
for digito in dez_digitos:
    RESULTADO_DIGITO_2 += int(digito) * CONTADOR_REGRESSIVO_2
    CONTADOR_REGRESSIVO_2 -= 1
digito_2 = (RESULTADO_DIGITO_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

CPF_GERADO_PELO_CALCULO = f"{nove_digitos}{digito_1}{digito_2}"

if cpf_enviado_usuario == CPF_GERADO_PELO_CALCULO:
    print(f"CPF: {cpf_enviado_usuario} é válido")
else:
    print("CPF inválido")
