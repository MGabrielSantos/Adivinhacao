import random


def jogar():
    print("***************")
    print("Bem vindo ao jogo de adivinhação")
    print("***************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) - Fácil (2) - Médio (3) - Difícil")

    nivel = int(input("Escolha um nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou o numero ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Chute inválido! Programa aceita somente números entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns, você acertou e a sua pontuação é: ", pontos)
            break
        else:
            if(maior):
                print("Você errou!, seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou!, seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()

