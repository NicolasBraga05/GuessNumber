# jogo para adivinhar o numero
from random import randint
def guessNumber():
    tentativa = 0
    pontos = 0
    print('*' * 10)
    print('JOGO DOS NUMEROS')
    print('*' * 10)
    print('Faca a maior quantidade de pontos com 3 chances de erro')
    escolha = int(input('1- Para jogar | 2- Para sair do programa: '))
    while True:
        if escolha == 1:
            NA = randint(1, 3)
            num = int(input(f'Informe um numero entre 1 e 3: '))
            print('*' * 10)
            if num == NA:
                print('Parabens, acertou de primeira!')
                print('+3 pontos')
                pontos += 3
            elif num != NA:
                print('Ops, numero incorreto')
                print('tente novamente')
                tentativa += 1
                num = int(input(f'Informe um numero entre 1 e 3: '))
                if num == NA:
                    print('Acertou na segunda!')
                    print('+2 pontos')
                    pontos += 2
                else:
                    print('Ops, numero incorreto')
                    print('tente novamente')
                    tentativa += 1
                    num = int(input(f'Informe um numero entre 1 e 3: '))
                    if num == NA:
                        print('Acertou na ultima tentativa!')
                        print('+1 ponto')
                        pontos += 1
                    else:
                        tentativa += 1
                        if tentativa >= 3:
                            print('Acabaram as tentativas :(')
                            print(f'Voce fez no total {pontos} pontos!!!')
                            break
        elif escolha == 2:
            print('Programa encerrado')
            break
        else:
            print('Informe uma opcao valida!')
            escolha = int(input('1- Para jogar | 2- Para sair do programa: '))



if __name__ == '__main__':
    guessNumber()



