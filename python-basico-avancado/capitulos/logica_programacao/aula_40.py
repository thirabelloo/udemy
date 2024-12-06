""" Calculadora com while """

while True:
    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operador = input("Digite o operador (+-/*): ")

    NUMEROS_VALIDOS = None
    NUM_1_FLOAT = 0
    NUM_2_FLOAT = 0

    try:
        NUM_1_FLOAT = float(numero_1)
        NUM_2_FLOAT = float(numero_2)
        NUMEROS_VALIDOS = True
    except ValueError:
        NUMEROS_VALIDOS = None

    if NUMEROS_VALIDOS is None:
        print("Um ou ambos os numeros digitados sao invalidos")
        continue

    OPERADORES_PERMITIDOS = "+-/*"

    if operador not in OPERADORES_PERMITIDOS:
        print("Operador invalidos")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")
    if operador == "+":
        print(f"{NUM_1_FLOAT} + {NUM_2_FLOAT} =", NUM_1_FLOAT + NUM_2_FLOAT)
    elif operador == "-":
        print(f"{NUM_1_FLOAT} - {NUM_2_FLOAT} =", NUM_1_FLOAT + NUM_2_FLOAT)
    elif operador == "/":
        print(f"{NUM_1_FLOAT} / {NUM_2_FLOAT} =", NUM_1_FLOAT + NUM_2_FLOAT)
    elif operador == "*":
        print(f"{NUM_1_FLOAT} * {NUM_2_FLOAT} =", NUM_1_FLOAT + NUM_2_FLOAT)

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    if sair is True:
        break
