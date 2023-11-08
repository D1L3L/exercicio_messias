import json
#Conte quantas linhas tem em cada um dos arquivos de texto.
#Depois, crie um novo arquivo de texto, informando qual o nome do livro e quantas linhas é possível encontrar dentro de cada um deles.
lista_livros = ["Moby-Dick.txt", 'the_prince.txt', 'The_Alchemist.txt', 'Frankenstein.txt']
qtd_pg = {'Moby-Dick.txt':'','the_prince.txt':'','The_Alchemist.txt':'','Frankenstein.txt': '' }
for i in range (len(lista_livros)):
    print(lista_livros[i])
    with open(lista_livros[i], 'r', encoding="UTF-8") as livro:
        linhas = livro.readlines()
        print ( f'A quantidade de linhas é {len(linhas)}')
        qtd_pg[lista_livros[i]] = len(linhas)
        
print (f"Tem {json.dumps(qtd_pg)} páginas")

with open('bloco.txt', 'w', encoding="UTF-8'") as bloco:
    ll = bloco.write(json.dumps(qtd_pg))
