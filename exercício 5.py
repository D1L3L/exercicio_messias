#Crie um programa que gere a sequência de Fibonacci até o décimo termo usando um loop while.
valores = [ 1, 1]
digitado = int(input("Informe qual termo você quer saber na sequência de Fibonacci: "))
termos = digitado
x = -1
y = 0
while (termos - 2) > 0:
    termos -= 1
    x += 1
    y += 1
    seq = valores[x] + valores[y]
    valores.append(seq)
print(f"Os termos são {valores}")
print (valores[digitado-1])