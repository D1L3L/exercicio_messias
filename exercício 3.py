#Faça um programa que calcule a soma de todos os números ímpares de 1 a 100 usando um loop while.
num = 0
res = 0
quantidade = []
while num < 100:
    
    if num % 2 != 0:
        res =  num + res
        quantidade.append(res)  
        print(res)
    num += 1
print (len(quantidade))
