#Escreva um programa que exiba os números pares, partindo de 2 até atingir um valor x informado pelo teclado. Se o valor
#informado for um número ímpar, então devem ser exibidos os números ímpares, partindo de 1 até atingir esse valor.
# Exemplos:

valor= int(input("informe um número final da sequência: "))

if valor % 2 == 0:
    for i in range(2,valor+1,2):
        print(i)

else:
    for i in range (1,valor+1,2):
        print(i)

print("outra forma de fazer é:")

if valor % 2 == 0:
    valorIni=2

else:
    valorIni=1

for k in range (valorIni,valor+1,2):
    print(k)