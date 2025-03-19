# Desenvolva um algoritmo em Python que receba dois números e exiba se são iguais ou diferentes.

# Dados:
  # ler dois números

# Processo
  # identificar o status

# Informação:
  #exibir status

num1 = float(input("Digite o primeiro número:"))

num2 = float(input("Digite o segundo número:"))

if num1 == num2:
  status = "Iguais"
else:
  status = "Diferentes"

print("Os números " + str(num1) + " e " + str(num2) + " são " + status)