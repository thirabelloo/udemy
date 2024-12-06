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

CPF = "746.824.890-70"
CPF_FORMATADO = CPF.replace(".", "").replace("-", "")
CPF_NOVE_DIGITOS = CPF_FORMATADO[:9]
CPF_DEZ_DIGITOS = CPF_FORMATADO[:10]

CONTAGEM_REGRESSIVA_PRIMEIRO_DIGITO = 10
CONTAGEM_REGRESSIVA_SEGUNDO_DIGITO = 11
SOMA_PRIMEIRO_DIGITO = 0
SOMA_SEGUNDO_DIGITO = 0

for i, digito in enumerate(CPF_NOVE_DIGITOS):
    SOMA_PRIMEIRO_DIGITO += int(digito) * (CONTAGEM_REGRESSIVA_PRIMEIRO_DIGITO - i)

multiplicacao = SOMA_PRIMEIRO_DIGITO * 10
RESULTADO = multiplicacao % 11

if RESULTADO > 9:
    print("O primeiro dígito do CPF é: 0")
else:
    print(f"O primeiro dígito do CPF é: {RESULTADO}")


for i, digito in enumerate(CPF_DEZ_DIGITOS):
    SOMA_SEGUNDO_DIGITO += int(digito) * (CONTAGEM_REGRESSIVA_SEGUNDO_DIGITO - i)

multiplicacao = SOMA_SEGUNDO_DIGITO * 10
RESULTADO_SEGUNDO_DIGITO = multiplicacao % 11

if RESULTADO_SEGUNDO_DIGITO > 9:
    print("O segundo dígito do CPF é: 0")
else:
    print(f"O segundo dígito do CPF é: {RESULTADO_SEGUNDO_DIGITO}")

CPF_GERADO_PELO_CALCULO = f"{CPF_NOVE_DIGITOS}{RESULTADO}{RESULTADO_SEGUNDO_DIGITO}"
print(CPF_GERADO_PELO_CALCULO)

if CPF_FORMATADO == CPF_GERADO_PELO_CALCULO:
    print(f"O CPF: {CPF_GERADO_PELO_CALCULO} é válido")
else:
    print(f"O CPF: {CPF_GERADO_PELO_CALCULO} é inválido")
