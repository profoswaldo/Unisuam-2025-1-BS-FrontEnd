# Faça um algoritmo em Python que receba a média de um aluno e 
# o número de exercícios extra-classe que realizou.
# O algorimto deverá exibir a nota do aluno e caso ele tenha 
# realizado mais de 8 exercícios, esta nota devera ser acrescida 
# em 1 ponto na média.

# Dados:
# media - ler
# nr exercicios realizados - ler
# ponto extra - atribuir 1

# processamento:
# calcular nova media

# Informação:
# media

media = float(input("Digite sua média: "))

exercicios = int(input("Digite o nr de exercícios realizados"))

ponto_extra = 1

media_final = media

if exercicios > 8:
    media_final = media + ponto_extra

print(media_final)



