"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os
import platform


def clear_screen():
    """
    Limpa a tela do terminal, dependendo do sistema operacional.
    """
    if platform.system() == ("Windows"):
        os.system("cls")
    else:
        os.system("clear")


lista_compras = []

while True:
    print("Selecione uma opcao")
    opcao_usuario = input("[i]nserir [a]pagar [l]istar [s]air: ").lower()

    if opcao_usuario in ("i", "inserir"):
        clear_screen()
        inserir_valor = input("Valor: ").title()
        lista_compras.append(inserir_valor)

    elif opcao_usuario in ("l", "listar"):
        clear_screen()
        if len(lista_compras) == 0:
            print("Nao tem itens no carrinho, por favor insira um item")
        else:
            print("Itens no carrinho:")
            for indice, nome_item in enumerate(lista_compras):
                print(indice, nome_item)

    elif opcao_usuario in ("a", "apagar"):
        clear_screen()
        if len(lista_compras) == 0:
            print("Nao tem item para apagar.")
        else:
            try:
                deletando_item = int(input("Escolha o indice para apagar: "))
                if 0 <= deletando_item < len(lista_compras):
                    del lista_compras[deletando_item]
                else:
                    print("Indice invalido.")
            except ValueError:
                print("Por favor, insira um numero valido.")

    elif opcao_usuario in ("s", "sair"):
        break

    else:
        print("Opcao invalida. Tente novamente.")
