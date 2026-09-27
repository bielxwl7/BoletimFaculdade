from dados import ALUNOS, PROFESSORES

def listar_alunos(professor):
    print("========== LISTA DE ALUNOS ==========")

    aluno_encontrado = False

    for matricula, aluno in ALUNOS.items():
        for disciplina in professor["diciplinas"]:
            if disciplina in aluno["disciplinas"]:
                notas = aluno["disciplinas"][disciplina]

                print(f"Matrícula: {matricula}")
                print(f"Nome: {aluno['nome']}")
                print(f"Curso: {aluno['curso']}")
                print(f"Disciplina: {disciplina}")
                print(f"Primeira nota: {notas['nota_1']}")
                print(f"Segunda nota: {notas['nota_2']}")
                print(f"Faltas: {notas['faltas']}")
                print("------------------------------------")

                aluno_encontrado = True

    if not aluno_encontrado:
        print("Nenhum aluno foi encontrado para suas disciplina.")