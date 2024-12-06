"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

PALAVRA_SECRETA = "thiago"
LETRA_ACERTADA = ""
NUMERO_TENTATIVA = 0


while True:
    letra_digitada = input("Digite uma letra: ")
    NUMERO_TENTATIVA += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digitada in PALAVRA_SECRETA:
        LETRA_ACERTADA += letra_digitada

    PALAVRA_FORMADA = ""
    for letra_secreta in PALAVRA_SECRETA:
        if letra_secreta in LETRA_ACERTADA:
            PALAVRA_FORMADA += letra_secreta
        else:
            PALAVRA_FORMADA += "*"
    print("Palavra formada: ", PALAVRA_FORMADA)

    if PALAVRA_FORMADA == PALAVRA_SECRETA:
        os.system("cls")
        print("VOCÊ GANHOU!! PARABÉNS!")
        print("A palavra era", PALAVRA_SECRETA)
        print("Tentativas:", NUMERO_TENTATIVA)
        LETRA_ACERTADA = ""
        NUMERO_TENTATIVA = 0
