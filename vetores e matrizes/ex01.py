# 1 - Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista).
#Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI,
#se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

times_brasileiros = ["Flamengo", 
"Palmeiras", "Santos", "Corinthians", 
"Grêmio", "Internacional", "Fluminense", 
"Cruzeiro", "Atlético Mineiro", "Botafogo"]

time = input("Digite mais um nome de clube: ")

if time in times_brasileiros:
    print("ACHEI")
else:
    print("NÃO ACHEI")