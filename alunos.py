from dados import ALUNOS, MEDIA_APROVACAO, MEDIA_RECUPERACAO

def acesso_aluno():
    print("Você entrou na área do aluno.")
    print("-------------------------------------")
    print("Digite abaixo sua matrícula e senha.")

    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    aluno = ALUNOS.get(matricula)

    if aluno is None:
        print("Aluno não encontrado")
        return
    if aluno["senha"] != senha:
        print("Senha incorreta.")
        return

    print("--------------------------------------")
    print(f"Seja bem-vindo, {aluno['nome']}!")
    print(f"Curso: {aluno['curso']}")
    print("--------------- BOLETIM --------------")

    for nome_disciplina, dados_disciplina in aluno["disciplinas"].items():
        nota_1 = dados_disciplina["nota_1"]
        nota_2 = dados_disciplina["nota_2"]
        faltas = dados_disciplina["faltas"]

        media = (nota_1 + nota_2) / 2

        if media >= MEDIA_APROVACAO:
            situacao = "Aprovado"
        elif media >= MEDIA_RECUPERACAO:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        print(f"Disciplina: {nome_disciplina}")
        print(f"Primeira nota: {nota_1}")
        print(f"Segunda nota: {nota_2}")
        print(f"Média: {media}")
        print(f"Faltas: {faltas}")
        print(f"Situação: {situacao}")
        print("------------------------------------")