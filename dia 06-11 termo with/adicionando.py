with open("arquivo.txt", "a") as file:
    conteudo = file.write("Olá mundo\n")
with open("arquivo.txt", "r") as file:
    print(file.readline())