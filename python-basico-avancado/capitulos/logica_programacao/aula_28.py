"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""


def obter_informacoes():
    """
    Solicita ao usuário que insira seu nome e idade,
    e então exibe várias informações sobre o nome fornecido.

    A função realiza as seguintes operações:
    1. Solicita o nome e a idade do usuário.
    2. Verifica se algum dos campos está vazio e, em caso afirmativo,
    exibe uma mensagem de erro e interrompe a execução.
    3. Exibe o nome do usuário.
    4. Exibe o nome do usuário invertido.
    5. Verifica se o nome contém espaços e informa o usuário.
    6. Exibe o número de letras no nome do usuário.
    7. Exibe a última letra do nome do usuário.
    """
    nome = input("Digite o seu nome: ").strip()
    if not nome or nome.isdigit():
        raise ValueError("Desculpe, o nome não pode ser vazio ou um número.")

    idade = input("Digite a sua idade: ").strip()
    if not idade:
        raise ValueError("Desculpe, a idade não pode ser vazia.")
    if nome.isdigit():
        raise ValueError("Desculpe, a idade deve ser um número.")

    idade = int(idade)
    if not 0 <= idade <= 100:
        raise ValueError("Desculpe, a idade deve ser um número entre 0 e 100.")

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print("Seu nome contém espacos")
    else:
        print("Seu nome nao contém espacos")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")


if __name__ == "__main__":
    obter_informacoes()
