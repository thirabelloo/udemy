"""Introducao ao for / in - estrutura de repeticao para coisas finitas"""

TEXTO = "Python"

i = 0
TAMANHO_STRING = len(TEXTO)

while i < TAMANHO_STRING:
    print(TEXTO[i])
    i += 1

SENHA_SALVA = "123456"
SENHA_DIGITADA = ""
REPETICOES = 0

while SENHA_SALVA != SENHA_DIGITADA:
    SENHA_DIGITADA = input(f"Sua senha ({REPETICOES}x): ")
    REPETICOES += 1

print("Aquele laco acima pode ter repeticoes infinitas")

TEXTO = "Python"
NOVO_TEXTO = ""

for letra in TEXTO:
    NOVO_TEXTO += f"*{letra}"
    print(letra)
print(NOVO_TEXTO)
