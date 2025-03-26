#Faça um programa em Python que receba a idade de 10 pessoas
#  e mostre quantas são maiores que 18 anos.


cont = 0
for i in range(1,11):
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        cont = cont + 1  # cont += 1

print(cont)