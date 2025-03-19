# A imobiliária Imóbilis vende apenas terrenos retangulares. 
# Faça um algoritmo para ler as dimensões de um terreno e 
# depois exibir a área do terreno.


# Dados:
# largura
# Comprimento

# Processamento:
# calcular area

# Informação:
# area


largura = input("Digite a largura do terreno: ")
comprimento = input("Digite o comprimento do terreno: ")

area = float(largura) * float(comprimento)

print("Area do terreno: " + str(area))