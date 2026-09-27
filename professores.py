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

def alterar_nota(professor):
    print("========== LANÇAMENTO DE NOTA ==========")

    matricula = input("Digite a matrícula do aluno: ")

    aluno = ALUNOS.get(matricula)

    if aluno is None:
        print("Aluno não encontrado")
        return

    disciplinas_disponiveis = []

    for disciplina in professor["disciplinas"]:
        if disciplina in aluno["disciplinas"]:
            disciplinas_disponiveis.append(disciplina)

    if not disciplinas_disponiveis:
        print("Você não ministra nenhuma disciplina para esse aluno.")
        return

    print("Escolha a disciplina: ")

    for numero, disciplina in enumerate(disciplinas_disponiveis, start=1):
        print(f"{numero} - {disciplina}")

    opcao_disciplina = input("Digite uma opção: ")

    if not opcao_disciplina.isdigit():
        print("Digite somente o número da opção")
        return

    numero_disciplina = int(opcao_disciplina)

    if numero_disciplina < 1 or numero_disciplina > len(disciplinas_disponiveis):
        print("Opção inválida.")
        return

    disciplina_escolhida = disciplinas_disponiveis[numero_disciplina - 1]

    print("Qual nota deseja lançar ou alterar?")
    print("1 - Primeira nota.")
    print("2 - Segunda nota.")

    opcao_nota = input("Digite uma opção: ")

    if opcao_nota == "1":
        campo_nota = "nota_1"
    elif opcao_nota == "2":
        campo_nota = "nota_2"
    else:
        print("Opção inválida.")
        return

    try:
        nova_nota = float(input("Digite a nova nota: ").replace(",", "."))

    except ValueError:
        print("A nota precisa ser um número")

    if nova_nota < 0 or nova_nota > 10:
        print("A nota precisa estar entre 0 e 10.")
        return

    dados_disciplina = aluno["disciplinas"][disciplina_escolhida]
    nota_anterior = dados_disciplina[campo_nota]

    dados_disciplina[campo_nota] = nova_nota

    print("Nota alterada com sucesso!")
    print(f"Aluno: {aluno['nome']}")
    print(f"Disciplina: {disciplina_escolhida}")
    print(f"Nota anterior: {nota_anterior}")
    print(f"Nova nota: {nova_nota}")