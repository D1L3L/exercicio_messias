#Crie um programa que imprima todos os números primos de 1 a 50 usando um loop for.
def eh_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

for num in range(51):
    if eh_primo(num):
        print(num)
