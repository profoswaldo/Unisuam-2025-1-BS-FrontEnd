# Faça um algoritmo em Python que receba o valor de um salario bruto e que calcule e exiba um salario liquido, descontanto 18% de Imposto de renda, caso o salario seja superior ou igual a R$ 3.000,00


# Processo:
  # calcular o salario_liquido

# Informação:
   # exbir salario_liquido



salario_bruto = float(input("Digite o salario bruto: "))

if salario_bruto >= 3000:
  ir = salario_bruto * 18/100
  salario_liquido = salario_bruto - ir
else:
  salario_liquido = salario_bruto

print("Salario Líquido é igual a " + str(salario_liquido))


