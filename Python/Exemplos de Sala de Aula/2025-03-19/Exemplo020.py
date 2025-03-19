# Implemente um algoritmo em Python que receba a matricula, nome, teste e prova de um aluno e que calcule e exiba a matricula, nome, média e qual o seu conceito conforme discriminado abaixo:

    # Conceito A - media superior ou igual a 9
    # Conceito B - media superior ou igual a 7 e inferior a 9
    # Conceito C - media superior ou igual a 5 e inferior a 7
    # Conceito D - media superior ou igual a 3 e inferior a 5
    # Conceito E - media inferior a 3

# Dados:
    # matricula - ler
    # nome - ler
    # teste - ler
    # prova - ler

# Processamento:
    # media - calcular
    # Conceito - Identificar

# Informação:
    # matricula - exibir
    # nome - exibir
    # media - exibir
    # conceito - exibir


matricula = input("Digite a matricula: ")
nome = input("Digite o seu nome: ")
teste = float(input("Digite a nota de teste: "))
prova = float(input("Digite a nota da prova: "))

media = (teste + prova) /2

if media >= 9:
  conceito = "A"
elif media >= 7:
     conceito = "B"
elif media >= 5:
     conceito = "C"
elif media >= 3:
     conceito = "D"
else:
     conceito = "E"

print("Matricula: " + matricula)
print("Nome:      " + nome)
print("Média:     " + str(media))
print("Conceito:  " + conceito)