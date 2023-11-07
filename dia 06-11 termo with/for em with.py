from time import sleep
#colocando for num termo with
with open('contagem.txt', 'a', encoding= 'UTF-8') as numero:
    
    for x in range(3):
        lista = input("Digite um número: ")
        lista = numero.write(lista)
print("só um minuto")
sleep(5)

with open('contagem.txt', 'r', encoding='UTF-8') as resultado:
    r = resultado.read()
    print(f"{r} ESSA É A LISTA")