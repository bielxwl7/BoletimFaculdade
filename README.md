# Boletim Faculdade

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/licen%C3%A7a-MIT-green?style=for-the-badge)

Sistema de boletim universitário executado no terminal, desenvolvido em Python para praticar organização de módulos, funções, estruturas condicionais, repetição e manipulação de dados.

O sistema possui áreas distintas para alunos e professores. Alunos podem consultar notas, médias, faltas e situação acadêmica. Professores podem acessar suas disciplinas, consultar alunos e lançar ou alterar notas.

## Funcionalidades

- Acesso separado para alunos e professores
- Autenticação por matrícula ou login e senha
- Consulta do boletim acadêmico
- Cálculo automático da média
- Exibição da situação do aluno: aprovado, recuperação ou reprovado
- Consulta de alunos por disciplina
- Lançamento e alteração de notas
- Validação de notas entre 0 e 10
- Controle de acesso às disciplinas de cada professor

## Tecnologias

- [Python 3](https://www.python.org/)
- Biblioteca padrão do Python
- Git e GitHub para versionamento

O projeto não possui dependências externas no momento.

## Estrutura do projeto

```text
boletimFaculdade/
├── alunos.py       # Autenticação e boletim dos alunos
├── boletim.py      # Ponto de entrada e menu principal
├── dados.py        # Cadastros e dados acadêmicos temporários
├── professores.py  # Autenticação e operações dos professores
├── LICENSE         # Licença do projeto
└── README.md       # Documentação
```

## Instalação

### Pré-requisitos

Antes de começar, instale:

- Python 3.10 ou superior
- Git, caso deseje clonar o repositório

### Obtenha o projeto

Clone o repositório e acesse sua pasta:

```bash
git clone <URL_DO_REPOSITORIO>
cd boletimFaculdade
```

Você também pode baixar o projeto como arquivo ZIP e extrair seu conteúdo.

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python boletim.py
```

No Windows, caso o comando anterior não esteja disponível, utilize:

```powershell
py boletim.py
```

## Uso

Ao iniciar o programa, escolha o tipo de acesso:

```text
1 - Sou um aluno
2 - Sou um professor
3 - Sair
```

### Área do aluno

Informe a matrícula e a senha cadastradas em `dados.py`. Após a autenticação, o sistema exibirá as disciplinas, notas, médias, faltas e situações acadêmicas.

### Área do professor

Informe o login e a senha cadastrados em `dados.py`. Após a autenticação, o professor poderá consultar seus alunos e lançar ou alterar notas nas disciplinas que ministra.

## Persistência dos dados

Nesta versão, os dados ficam armazenados em estruturas Python dentro de `dados.py`. Alterações realizadas durante a execução não são preservadas depois que o programa é encerrado.

Uma versão futura poderá utilizar SQLite para salvar usuários, disciplinas, notas e alterações permanentemente.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.

---

Desenvolvido por Gabriel Costa.
