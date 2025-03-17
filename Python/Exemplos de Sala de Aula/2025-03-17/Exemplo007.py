matricula = input("Digite a matricula: ")
nome = input("Digite o nome: ")
salBruto = float(input("Digite o salario Bruto: "))

salLiq = salBruto - salBruto * 11 / 100 

print("Matricula: ", matricula)
print("Nome: ", nome)
print("Salário Líquido: ", salLiq)


