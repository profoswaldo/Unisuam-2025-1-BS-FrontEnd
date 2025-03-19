# Tendo como dados de entrada a altura e o sexo de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando 
# as seguintes fórmulas:

    # ● para homens: (72.7 * altura) – 58;
    # ● para mulheres: (62.1 * altura) – 44.7.


altura = float(input("Digite a sua altura: "))
sexo = input("Digite M para masculino e F para feminino: ")


if sexo == "M":
  peso_ideal = (72.7 * altura) - 58
else:
  peso_ideal = (62.1 * altura) - 44.7

print("Seu peso ideal é " + str(peso_ideal))