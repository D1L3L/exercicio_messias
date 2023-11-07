#faz a leitura do arquivo
with open('arquivo.txt', "r", encoding= 'UTF-8') as file:
    conteudo = file.read()
print (conteudo)

with open("arquivo.txt", "w", encoding= 'UTF-8') as file:
    conteudo = file.write()
print (conteudo)
#adiciona arquivo 
with open("arquivo.txt", "a", encoding='UTF-8') as file:
    conteudo = file.write("Olá mundo")

print(conteudo)