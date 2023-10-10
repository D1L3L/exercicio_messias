clubes_de_futebol = ["Flamengo", 
"Palmeiras", "Santos", "Corinthians", 
"Grêmio", "Internacional", "Fluminense", 
"Cruzeiro", "Atlético Mineiro", "Botafogo"]


clube_pesquisado = input('Digite o clube: ')

for clube in clubes_de_futebol:

    if clube == clube_pesquisado:
        print('Achei')
        break
    else:
        print('Ainda não achei!')
        