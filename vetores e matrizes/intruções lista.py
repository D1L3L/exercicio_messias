# Lista de frutas

frutas = ["pêra", "uva", "maçã", "kiwi"]

# Alterando o elemento que está na posição 1
print (frutas)
frutas[1] = "abacate"
print (frutas)

#O método insert() ajuda você a adicionar um elemento em qualquer posição desejada.

frutas.insert(len(frutas),"morango")
print (len(frutas))
print (frutas)

frutas.remove("kiwi")
print (frutas)
print (len(frutas))

for fruteira in frutas:
    print (f"A fruta mais saborosa é {frutas()}")
