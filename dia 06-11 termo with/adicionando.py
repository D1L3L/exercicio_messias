with open("arquivo.txt", "a", encoding='UTF-8') as file:
    conteudo = file.write("Olá mundo\n")
print(conteudo)
