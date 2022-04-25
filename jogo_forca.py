import random
palavras = ['rato','gato','mico','baleia']
escolha = random.choice(palavras)
alfa = ['q','w','e','r','t','y','u','i','o',
        'p','a','d',
        'f','g','h','j','k','l','ç','z',
        'x','c','v','b','m','s','n']
tentativas = 0
chances = 7
acertos = 0
letras_escolhidas = []
estado_palavra = ['_' ] * len(escolha)


print('--jogo da forca--')
print('dicas: É UM ANIMAL!')
print(f"o tamanho da palavra{estado_palavra}")
print(escolha)


if __name__ == '__main__':
    while chances>tentativas :
        jogadas = str(input(('Digite uma letra: '))).lower()
        if jogadas not in alfa:
            print("Isso não é uma letra, tente novamente!")
            continue
        elif jogadas in alfa:

            if jogadas in escolha:
                print("Parabéns, vocè acertou a letra!")
                for i in range(len(escolha)):
                    if jogadas==escolha[i]:
                        estado_palavra[i] =jogadas
                        for x in estado_palavra:
                                print(x,end='')
                        acertos+=1
                    if acertos<len(estado_palavra):
                        continue
                    else:
                        print("Parabéns!,você ganhou o jogo da forca!")
                        tentativas = chances + 1
                        break
            else:
                tentativas+=1
                letras_escolhidas.append(jogadas)
                print('As letras jogadas foram:', end='')
                for item in letras_escolhidas:
                    print('',item , end='')
                print('\nVocê tem ', chances - tentativas,'jogadas')
                if tentativas>chances:
                    print(f'Você perdeu o jogo!,a palavra da forca era{escolha}')
                    break




