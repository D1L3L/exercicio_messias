#Crie um programa que peça ao usuário uma palavra e imprima cada letra em uma linha usando um loop for.
palavra = str(input("Digite uma palavra: "))
letras = len(palavra)
for x in range(letras):
    print (palavra[x])