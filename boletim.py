from alunos import acesso_aluno
from professores import acesso_professor

print("========== SISTEMA DE NOTAS - UNIESP ==========")
print("Seja bem-vindo ao sistema de boletim da UNIESP!")
print("--------------------------------------------------")
print("Você é um aluno ou professor?")
print("Escolha uma das opções abaixo:")
print("1 - Sou um Aluno.")
print("2 - Sou um professor.")
print("3 - Sair.")

selecionado = input("Digite aqui: ")

if selecionado == "1":
    acesso_aluno()
elif selecionado == "2":
    acesso_professor()
elif selecionado == "3":
    print("Saindo...")
    exit()
else:
    print("Opção inválida.")
    exit()