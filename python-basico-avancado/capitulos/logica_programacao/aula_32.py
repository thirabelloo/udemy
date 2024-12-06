""" Exercícios - Lógica de Programação"""


def verificar_numero_par_impar():
    """
    Solicita ao usuário que digite um número inteiro e informa se o número é par ou ímpar.

    A função solicita ao usuário que insira um número. Se o número inserido for um inteiro,
    a função verifica se ele é par ou ímpar e imprime a mensagem correspondente. Se o valor
    inserido não for um número inteiro, a função exibe uma mensagem de erro.

    Exemplo de uso:
    verificar_numero_par_impar()
    """
    numero = input("Digite um numero inteiro: ")

    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"O numero {numero} é par")
        else:
            print(f"O numero {numero} é impar")
    except ValueError:
        print("Erro: O valor deve ser um número inteiro.")


def verificar_tamanho_nome():
    """
    Pede ao usuário que digite seu primeiro nome e avalia o tamanho do nome.
    Se o nome tiver 4 letras ou menos, imprime "Seu nome é curto".
    Se o nome tiver entre 5 e 6 letras, imprime "Seu nome é normal".
    Se o nome tiver mais de 6 letras, imprime "Seu nome é muito grande".
    """
    nome = input("Digite seu primeiro nome: ").strip()

    if not nome:
        print("Erro: O campo não pode estar vazio.")
        return

    if not nome.isalpha():
        print("O nome deve conter apenas letras.")
        return

    tamanho_nome = len(nome)
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif 5 <= tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")


def imprimir_saudacao():
    """
    Pergunta a hora ao usuário e exibe a saudação apropriada com base no horário informado.
    Saudações:
    - Bom dia: 00:00 - 11:59
    - Boa tarde: 12:00 - 17:59
    - Boa noite: 18:00 - 23:59

    Se o valor informado não for um número inteiro ou estiver fora do intervalo de 0 a 23,
    uma mensagem de erro será exibida.
    """
    hora = input("Digite que hora em números inteiros: ")

    try:
        hora = int(hora)
        if 0 <= hora <= 11:
            print("Bom dia")
        elif 12 <= hora <= 17:
            print("Boa tarde")
        elif 18 <= hora <= 23:
            print("Boa noite")
        else:
            print("Hora inválida")
    except ValueError:
        print("Erro: A hora deve ser um número inteiro.")


if __name__ == "__main__":
    verificar_numero_par_impar()
    verificar_tamanho_nome()
    imprimir_saudacao()
