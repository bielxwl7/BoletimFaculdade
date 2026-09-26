from dados import PROFESSORES

def acesso_professor():
    print("Você entrou na área do professor.")
    print("Digite abaixo seu login e senha.")

    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    professor = PROFESSORES.get(login)

    if professor is None:
        print("Professor não encontrado")
        return
    if professor["senha"] != senha:
        print("Senha incorreta.")
        return

    print("--------------------------------------")
    print(f"Seja bem-vindo, {professor['nome']}!")