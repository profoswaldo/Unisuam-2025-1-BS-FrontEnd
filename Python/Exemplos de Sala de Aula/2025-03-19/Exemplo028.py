# Faça um algoritmo que leia uma variável e some 5 caso seja 
# par ou some 8 caso seja ímpar, imprimir o resultado desta operação.


valor = int(input("Digite um valor: "))

if valor%2 != 0:
  resultado = valor + 8
else:
  resultado = valor + 5

print("Resultado = " + str(resultado))
