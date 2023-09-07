#Escreva um programa que solicite ao usuário uma senha e continue pedindo até que a senha digitada seja igual a "senha123".
senha = str(input("Digite a senha em 1 2 3: "))
while senha != "senha123":
    senha = str(input("Tente digitar a senha novamente: "))

print("Ótimo, a senha está correta! (❁´◡`❁)")