# A prefeitura de uma cidade fez uma pesquisa com 200 pessoas, 
# coletando dados sobre o salário e o número de filhos. 
# A prefeitura deseja saber: 
#    • A média do salário dessas pessoas 
#    • A média do número de filhos 
#    • O maior salário 
#    • A percentagem de pessoas com salários até R$ 150,00

cont=0
somafilhos=0
somasalario=0

for i in range(1,3):
  salario = float(input("Digite o salario"))
  nrfilhos = int(input("Digite o numero de filhos: "))
  somasalario+= salario # somasalario = somasalario + salarios
  somafilhos+=nrfilhos # somafilhos = somafilhos + nrfilhos
  if i==1:
    maior = salario
  else:
    if maior<salario:
      maior = salario  
  if salario<=150:
    cont = cont + 1


print(somasalario/i)
print(somafilhos/i)
print(maior)
print(cont*100/i)

