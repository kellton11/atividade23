# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.

num = int(input("digite um número para exebir sua tabuada: "))

for x in range(11):
    print("{} x {} = {}".format(num,x,num*x))