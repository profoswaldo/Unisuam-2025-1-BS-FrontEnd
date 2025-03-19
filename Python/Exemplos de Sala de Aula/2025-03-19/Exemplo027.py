# Faça um algoritmo para receber um número qualquer e 
# informar na tela se é par ou ímpar.


numero = int(input("Digite um número: "))

if numero%2==0:
  resultado = "par"
else:
  resultado = "impar"

print("Número " + str(numero) + " é " + resultado)