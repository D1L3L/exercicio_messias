nomes_arquivos = ["Moby_Dick.txt, the_prince.txt, The_Alchemist.txt, Frankenstein.txt"]

with open("informacoes_livros.txt", "w", encoding="UTF-8") as arquivo_saida:

    for nome_arquivo in nomes_arquivos:
 
        with open(nome_arquivo, "r", encoding="UTF-8") as arquivo_livro:

            linhas = arquivo_livro.readlines()
            num_linhas = len(linhas)
            

            arquivo_saida.write(f"Nome do Livro: {nome_arquivo}, Linhas: {num_linhas}\n")

# O arquivo "informacoes_livros.txt" agora contém as informações sobre os livros.
