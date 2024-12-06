""" Criando um gerador de CPFs com nosso algoritmo e Python"""

import random


for _ in range(100):
    NOVE_DIGITOS = ""
    for i in range(9):
        NOVE_DIGITOS += str(random.randint(0, 9))

    print(NOVE_DIGITOS)

    # CONTADOR_REGRESSIVO_1 = 10

    # RESULTADO_DIGITO_1 = 0
    # for digito in nove_digitos:
    #     RESULTADO_DIGITO_1 += int(digito) * CONTADOR_REGRESSIVO_1
    #     CONTADOR_REGRESSIVO_1 -= 1
    # digito_1 = (RESULTADO_DIGITO_1 * 10) % 11
    # digito_1 = digito_1 if digito_1 <= 9 else 0

    # dez_digitos = nove_digitos + str(digito_1)
    # CONTADOR_REGRESSIVO_2 = 11

    # RESULTADO_DIGITO_2 = 0
    # for digito in dez_digitos:
    #     RESULTADO_DIGITO_2 += int(digito) * CONTADOR_REGRESSIVO_2
    #     CONTADOR_REGRESSIVO_2 -= 1
    # digito_2 = (RESULTADO_DIGITO_2 * 10) % 11
    # digito_2 = digito_2 if digito_2 <= 9 else 0

    # cpf_gerado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"
    # print(cpf_gerado_pelo_calculo)
