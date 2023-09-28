#A conversão de graus Fahrenheit para Celsius é obtida pela fórmula: (C=F-32/1,8)Escreva um programa que calcule e
# apresente uma tabela de graus Celsius em função de graus Fahrenheit que variem de 50 a 150, de 1 em 1.

for i in range(50,150):
    print(i, "Fº e ",(i-32)/1.8 ,"Cº")