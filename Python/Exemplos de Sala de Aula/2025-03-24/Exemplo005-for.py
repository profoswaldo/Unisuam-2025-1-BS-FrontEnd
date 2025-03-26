qtAlunos = int(input("Digite a quantidade de alunos: "))
for i in range(qtAlunos):
    matricula = input("Digite a matricula do aluno: ")
    nome=input("Digite o nome do aluno: ")
    teste=float(input("Digite a nota de teste do aluno: "))
    prova=float(input("Digite a nota da prova do aluno: "))

    media=(teste + prova)/2

    print("Matricula: ", matricula)
    print("Nome: ", nome)
    print("Média: ", media)