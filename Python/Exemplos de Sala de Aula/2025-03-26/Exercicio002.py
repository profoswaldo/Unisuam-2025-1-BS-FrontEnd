# Faça um programa em Python leia 10 valores inteiros e: 
#    • Encontre e mostre o maior valor 
#    • Encontre e mostre o menor valor 
#    • Calcule e mostre a média dos números lidos


somavalor = 0

for i in range(1,11):
    valor = int(input("Digite valor : "))
    if i==1:
        maior = valor
        menor = valor
    else:
        if maior < valor:
            maior = valor
        if menor > valor:
            menor = valor

    somavalor = somavalor + valor

print(maior)
print(menor)
print(somavalor/i)