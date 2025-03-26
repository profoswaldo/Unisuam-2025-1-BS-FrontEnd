
# Desenvolver um programa Python que leia um número não determinado de valores e 
# calcule e escreva a média aritmética dos valores lidos, a quantidade de 
# valores positivos, a quantidade de valores negativos e o percentual de valores 
# negativos e positivos


## Dados
    ## valor - ler

# processo
    ## Calcular Media 
    ## Calcular qt Positivos
    ## Calcular qt Negativos 
    ## Calcular percentual valores Positivos
    ##S Calcular Percentual valores Negativos



#Informação
    ## Exibir Media 
    ## Exibir qt Positivos
    ## Exibir qt Negativos 
    ## Exibir percentual valores Positivos
    ## Exibir Percentual valores Negativos

soma = 0
cont = 0
qtPositivos = 0
qtNegativos = 0

opcao = input("Digite S para entrar com um valor ou qualquer outro caracter para finalizar o programa: ")
while opcao == "S":
    valor=int(input("Digite um valor: "))
    soma = soma + valor
    cont = cont + 1
    if valor>0:
        qtPositivos = qtPositivos + 1
    else:
        qtNegativos = qtNegativos + 1


    opcao = input("Digite S para entrar com um valor ou qualquer outro caracter para finalizar o programa: ")


media = soma/cont
print("Média: ", media)


print("Quantidade de Positivos: ", qtPositivos)
print("Quantidade de Negativos: ", qtNegativos)


percPositivos = qtPositivos*100/cont
percNegativos = qtNegativos*100/cont

print("Percentual nr Positivos: ", percPositivos)
print("Percentual nr Negativos: ", percNegativos)
