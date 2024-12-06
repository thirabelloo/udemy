"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
-  10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
-  70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

CPF = "746.824.890-70"
CPF_FORMATADO = CPF.replace(".", "").replace("-", "")
CPF_NOVE_DIGITOS = CPF_FORMATADO[:9]

CONTAGEM_REGRESSIVA_PRIMEIRO_DIGITO = 10
SOMA_PRIMEIRO_DIGITO = 0

for i, digito in enumerate(CPF_NOVE_DIGITOS):
    SOMA_PRIMEIRO_DIGITO += int(digito) * (CONTAGEM_REGRESSIVA_PRIMEIRO_DIGITO - i)

multiplicacao = SOMA_PRIMEIRO_DIGITO * 10
RESULTADO_DIGITO_UM = multiplicacao % 11

if RESULTADO_DIGITO_UM > 9:
    print("O primeiro dígito do CPF é: 0")
else:
    print(f"O primeiro dígito do CPF é: {RESULTADO_DIGITO_UM}")
