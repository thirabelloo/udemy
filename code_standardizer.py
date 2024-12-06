"""Script de padronizacao de codigo"""

import argparse
import subprocess


def parse_args():
    """
    Analisa os argumentos da linha de comando.

    Retorna:
        argparse.Namespace: Um objeto Namespace contendo os argumentos e seus valores.
    """
    parser = argparse.ArgumentParser(description="Script de padronizacao de codigo")
    parser.add_argument("--flake8", action="store_true", help="Executa o Flake8")
    parser.add_argument("--black", action="store_true", help="Executa o Black")
    parser.add_argument("--pylint", action="store_true", help="Executa o Pylint")
    parser.add_argument("--vulture", action="store_true", help="Executa o Vulture")
    parser.add_argument(
        "--all", action="store_true", help="Executa todas as ferramentas"
    )
    return parser.parse_args()


def run_command(command, check):
    """
    Executa um comando no subprocesso e imprime a saída.

    Args:
        command (list): Lista de strings que representam o comando e seus argumentos.
        check (bool): Se True, levanta uma exceção se o comando retornar um código de erro.

    Raises:
        subprocess.CalledProcessError: Se o comando retornar um código de erro e check for True.
        FileNotFoundError: Se o comando não for encontrado.
        OSError: Para outros erros relacionados ao sistema operacional.
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=check)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as error:
        print(f"Erro ao executar {command[0]}: {error.stderr}")
    except FileNotFoundError:
        print(f"Comando não encontrado: {command[0]}")
    except OSError as e:
        print(f"Erro inesperado ao executar {command[0]}: {str(e)}")


def run_flake8():
    """
    Executa o Flake8 para análise de código.
    """
    print("Running Flake8...")
    run_command(["flake8", "--exclude=.venv", "."], check=False)


def run_black():
    """
    Executa o Black para formatação de código.
    """
    print("Running Black...")
    run_command(["black", "--exclude=.venv", "."], check=False)


def run_pylint():
    """
    Executa o Pylint para análise de código.
    """
    print("Running Pylint...")
    run_command(["pylint", "."], check=False)


def run_vulture():
    """
    Executa o Vulture para encontrar código morto.
    """
    print("Running Vulture...")
    run_command(["vulture", "--exclude=.venv", "."], check=False)


if __name__ == "__main__":
    print("Script iniciado...")
    args = parse_args()
    if args.all or args.flake8:
        run_flake8()
    if args.all or args.black:
        run_black()
    if args.all or args.pylint:
        run_pylint()
    if args.all or args.vulture:
        run_vulture()
