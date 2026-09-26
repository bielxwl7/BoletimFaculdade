from dados import PROFESSORES

def acesso_professor():
    print("Você entrou na área do professor.")
    print("Digite abaixo seu login e senha.")

    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    print(f"Seja bem vindo {login}! O que deseja fazer?")