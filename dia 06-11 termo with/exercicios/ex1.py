#Crie um programa Python que imprima todas as linhas deste aquivo;
#E conte quantas linhas tem neste aquivo.

with open('Frankenstein.txt', 'a', encoding="UTF-8") as livro:
    linhas = livro.write()
    print ( f'A quantidade de linhas é {len(linhas)}')
    
