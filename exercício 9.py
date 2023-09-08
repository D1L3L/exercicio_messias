#Escreva um programa que conte quantas vezes a letra "a" aparece em uma string usando um loop for.
palavras = str(input("Digite uma palavra: "))
letras = (len(palavras))
contador = 0
for x in range(letras):
    if (palavras[x]) == "a" or (palavras[x]) == "á" or (palavras[x]) == "à" or (palavras[x]) == "â":
        contador += 1
if contador == 1:
    print (f"A palavra digitada foi {palavras} ela possui {letras} letras, e contém apenas {contador} letra a.")
elif contador > 1:
    print (f"A palavra digitada foi {palavras} ela possui {letras} letras, e contém {contador} letras a.")
else:
    print (f"A palavra digitada foi {palavras} ela possui {letras} letras, mas não contém letras a.")
