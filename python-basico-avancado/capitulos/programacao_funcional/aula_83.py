"""Exercicio - Sistema de perguntas e respostas"""

perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opcoes": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opcoes": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opcoes": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

QUANTIDADE_ACERTOS = 0

for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opcoes"]
    for i, opcao in enumerate(opcoes):
        print(f"{i})", opcao)
    print()

    escolha = input("Escolha uma opcao: ")

    ESCOLHA_INT = None
    ACERTOU = False
    # quantidade_opcoes = len(opcoes)

    if escolha.isdigit():
        ESCOLHA_INT = int(escolha)

    if ESCOLHA_INT is not None and 0 <= ESCOLHA_INT < len(opcoes):
        if opcoes[ESCOLHA_INT] == pergunta["Resposta"]:
            ACERTOU = True

    print()
    if ACERTOU:
        QUANTIDADE_ACERTOS += 1
        print("Acertou❤️")
    else:
        print("Errou❌")

print(f"Você acertou: {QUANTIDADE_ACERTOS} de {len(perguntas)} perguntas")
