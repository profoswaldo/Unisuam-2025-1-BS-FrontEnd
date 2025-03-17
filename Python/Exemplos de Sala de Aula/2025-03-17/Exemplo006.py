matricula = input("Digite a matricula: ")
nome = input("Digite o nome: ")
salBruto = float(input("Digite o salario Bruto: "))

inss = salBruto * 11 / 100 # salBruto * 0.11
salLiq = salBruto - inss

print("Matricula: ", matricula)
print("Nome: ", nome)
print("Salário Líquido: ", salLiq)


