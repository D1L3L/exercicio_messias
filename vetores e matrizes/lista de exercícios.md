Desenvolva os algoritmos abaixo em linguagem Python. Utilize o VS Code ou Pycharm, mas ao final entregue ao professor um arquivo .py para cada questão desenvolvida. As atividades deverão ser entregues no Github.
Vetores
Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.
Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.
Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;
Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.
Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] + B[0] deverá ser salva em N[0].
Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).
Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.
Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.
Matrizes
Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados). A seguir, leia um número X e escreva uma mensagem indicando se o valor de X existe ou NÃO na matriz.
DESAFIO | Construa uma matriz 10 x 10 com valores randômicos. A matriz não pode ter valores repetidos. Depois apresente:
o resultado da soma de todos os valores da matriz;
o resultado da soma dos valores da diagonal principal;
o resultado da soma dos valores da diagonal secundária;
o resultado da soma da coluna central;
Leia uma matriz 10 x 10 e escreva a localização (linha e a coluna) do maior valor.
Tuplas e Dicionários
Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu dicionário.
Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e pergunte quais seus número favoritos. Use seus nomes para serem as chaves de cada número favorito. Ao final, exiba o nome de cada pessoas e seu número favorito.
Dado uma lista de números, crie um algoritmo que retorne a soma dos números pares na lista.
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Saída esperada: 12
Dado uma lista de strings, crie um algoritmo que retorne a lista de strings ordenada por ordem decrescente de tamanho.
Exemplo de entrada: ['casa', 'carro', 'abacate', 'pipoca']
Saída esperada: ['abacate', 'carro', 'casa', 'pipoca']
Dado uma tupla de tuplas, onde cada tupla interna representa um intervalo de tempo (horário de início e horário de término), crie um algoritmo que retorne a quantidade de horas total dos intervalos.
Exemplo de entrada: ((8, 12), (14, 18), (19, 22))
Saída esperada: 11
Dado uma lista de dicionários, onde cada dicionário representa um produto com as chaves "nome", "preço" e "quantidade", crie um algoritmo que retorne o valor total do estoque.
Exemplo de entrada: [{'nome': 'maçã', 'preço': 2.0, 'quantidade': 5}, {'nome': 'banana', 'preço': 1.5, 'quantidade': 10}]
Saída esperada: 25.0
Dado duas listas, crie um algoritmo que retorne a interseção dos elementos das duas listas (ou seja, os elementos que aparecem nas duas listas).
Exemplo de entrada: [1, 2, 3, 4], [3, 4, 5, 6]
Saída esperada: [3, 4]
Dado um dicionário com as chaves representando nomes de países e os valores sendo listas de nomes de cidades, crie um algoritmo que retorne a cidade mais populosa de cada país em um novo dicionário.
Exemplo de entrada: {'Brasil': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'], 'EUA': ['Nova Iorque', 'Los Angeles', 'Chicago']}
Saída esperada: {'Brasil': 'São Paulo', 'EUA': 'Nova Iorque'}
Dado uma lista de tuplas, onde cada tupla representa um ponto no espaço tridimensional (coordenadas x, y e z), crie um algoritmo que retorne a distância total percorrida ao conectar todos os pontos na ordem em que aparecem na lista.
Exemplo de entrada: [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
Saída esperada: 9.48 (aproximadamente)
Dado um dicionário representando um grafo direcionado, onde as chaves são os vértices e os valores são listas de vértices adjacentes, crie um algoritmo que retorne o caminho mais curto entre dois vértices usando o algoritmo de Dijkstra.
Exemplo de entrada: {'A': {'B': 1, 'C': 4}, 'B': {'D': 3}, 'C': {'D': 2}, 'D': {}}, 'A', 'D'
Saída esperada: ['A', 'B', 'D']
Dado uma lista de strings, crie um algoritmo que retorne a palavra mais frequente na lista.
Exemplo de entrada: ['azul', 'vermelho', 'verde', 'azul', 'vermelho', 'amarelo', 'azul']
Saída esperada: 'azul'
Dado uma lista de dicionários, onde cada dicionário representa um filme com as chaves "título", "ano" e "gênero", crie um algoritmo que retorne a lista de filmes ordenada primeiro por gênero e depois por ano.
Exemplo de entrada: [{'título': 'O Poderoso Chefão', 'ano': 1972, 'gênero': 'drama'}, {'título': 'Pulp Fiction', 'ano': 1994, 'gênero': 'drama'}, {'título': 'Indiana Jones e os Caçadores da Arca Perdida', 'ano': 1981, 'gênero': 'aventura'}, {'título': 'De Volta Para o Futuro', 'ano': 1985, 'gênero': 'aventura'}]
Saída esperada: [{'título': 'Indiana Jones e os Caçadores da Arca Perdida', 'ano': 1981, 'gênero': 'aventura'}, {'título': 'De Volta Para o Futuro', 'ano': 1985, 'gênero': 'aventura'}, {'título': 'O Poderoso Chefão', 'ano': 1972, 'gênero': 'drama'}, {'título': 'Pulp Fiction', 'ano': 1994, 'gênero': 'drama'}]
