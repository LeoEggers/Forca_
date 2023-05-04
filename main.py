from random import choice
import pygame
from time import sleep


def tent(t):
    if t == 6:
        print("  _____")
        print(" |     |")
        print(" |      ")
        print(" |")
        print(" |")
        print("_|_")

    if t == 5:
        print("  _____")
        print(" |     |")
        print(" |     O")
        print(" |      ")
        print(" |     ")
        print("_|_")

    if t == 4:
        print("  _____")
        print(" |     |")
        print(" |     O")
        print(" |     |")
        print(" |")
        print("_|_")

    if t == 3:
        print("  _____")
        print(" |     |")
        print(" |     O")
        print(" |    /|")
        print(" |")
        print("_|_")

    if t == 2:
        print("  _____")
        print(" |     |")
        print(" |     O")
        print(" |    /|\\")
        print(" |")
        print("_|_")

    if t == 1:
        print("  _____")
        print(" |     |")
        print(" |     O")
        print(" |    /|\\")
        print(" |    /")
        print("_|_")
    if t == 0:
        print("  _____")
        print(" |     |")
        print(" |     O")
        print(" |    /|\\")
        print(" |    / \\")
        print("_|_")


def verde(msg):
    return f'\033[1;32m{msg}\033[m'


def vermelho(msg):
    return f'\033[1;31m{msg}\033[m'


# Carrega os áudios.
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('trilha.mp3')
pygame.mixer.music.play(-1)
confirma = pygame.mixer.Sound('confirma.mp3')
correto = pygame.mixer.Sound('correto.mp3')
erro = pygame.mixer.Sound('erro.mp3')
vitoria = pygame.mixer.Sound('victory.mp3')
gameover = pygame.mixer.Sound('gameover.mp3')
tentenovamente = pygame.mixer.Sound('tentenovamente.mp3')
encerrar = pygame.mixer.Sound('encerrar.mp3')

# Carrega as palavras e cria as listas das dificuldades.
palavras = open("Lista-de-Palavras.txt")
facil = []
medio = []
dificil = []

# Lista para converter caractere para caractere acentuado automaticamente.
acento = {'A': ['Á', 'Ã', 'Â'], 'E': ['É', 'Ê'], 'I': ['Í'], 'O': ['Ó', 'Õ', 'Ô'], 'U': ['Ú'], 'C': ['Ç']}

# Cria uma lista de emojis para erros e acertos.
emo_acerto = ['😍', '😁', '🤗', '👏', '🙌', '🤞', '☺️']
emo_erro = ['😬', '😱', '😰', '😓', '😭', '😨', '😖']

# Carrega a lista das dificuldades por extensão.
for line in palavras:
    line = line.strip()
    if 2 < len(line) <= 5:
        facil.append(line)
    elif 5 < len(line) <= 8:
        medio.append(line)
    elif len(line) > 8:
        dificil.append(line)

# Inicia o jogo e escolhe a dificuldade.
while True:
    # Escolhe o número de jogadores.
    while True:
        md = ['1', '2']
        modo = input('Escolha o número de jogadores [1/2]: ').strip()
        if modo in md:
            modo = modo[0]
            confirma.play()
            break
        print('Tente novamente.')
        tentenovamente.play()

    # Modo 2 jogadores: um dos jogadores escolhe a palavra.
    if modo == '2':
        palavra = input('Escolha uma palavra: ').strip().upper()
        confirma.play()

    # Modo 1 jogador: palavra escolhida aleatoriamente, o jogador escolhe a dificuldade.
    else:
        while True:
            d = ['F', 'M', 'D']
            dif = input('Dificuldade[F][M][D]: ').strip().upper()
            if dif in d:
                dif = dif[0]
                confirma.play()
                break
            print('Tente novamente.')
            tentenovamente.play()

        if dif == 'F':
            palavra = choice(facil)
        elif dif == 'M':
            palavra = choice(medio)
        else:
            palavra = choice(dificil)

    # Cria uma sequência de underlines, um para cada letra da palavra escolhida.
    # Cria as listas tem/não tem, estabelece o número de tentativas.
    tentativas = 7
    resp = ['_' for letra in palavra]
    lista_naotem = []
    lista_tem = []

    # Começa o jogo / coleta e trata o palpite.
    while True:
        print(' '.join(resp))
        palpite = input('Letra: ').strip().upper()

        if not palpite.isalpha() and palpite != '-':
            print('Você não digitou uma letra. Tente novamente.')
            tentenovamente.play()
            continue
        else:
            palpite = palpite[0]

        if palpite in lista_tem or palpite in lista_naotem:
            print('Você já tentou essa letra!')
            tentenovamente.play()
            continue

        # Substitui caracteres sem acento por caracteres acentuados, caso existam.
        passe = False
        if palpite in acento:
            for ltr in acento[palpite]:
                if ltr in palavra:
                    lista_tem.append(ltr)
                    resp[palavra.index(ltr)] = ltr
                    passe = True

        if palpite in palavra or passe:  # o passe serve para aceitar o caractere acentuado como se fosse sem acento.
            lista_tem.append(palpite)
            correto.play()
            print(verde('Acertou!'), f'{choice(emo_acerto)}')
            for indice, letra in enumerate(palavra):
                if letra == palpite:
                    resp[indice] = palpite
            if '_' not in resp:
                pygame.mixer.music.stop()
                vitoria.play()
                print(' '.join(resp))
                print(verde('Parabéns! Você venceu!'), '🥳😎✨🏆🎊🎉')
                break
        else:
            lista_naotem.append(palpite)
            erro.play()
            print(f'{lista_naotem}')
            tentativas -= 1
            print(vermelho('Errou!'), f'{choice(emo_erro)}'
                                      f'\n Tentativas restantes: {tentativas}')
            tent(tentativas)  # Mostra a forca
            if tentativas == 0:
                print(vermelho('Você perdeu...'), f'☠️💔😢🥀💥 A palavra era {palavra}.')
                pygame.mixer.music.stop()
                gameover.play()
                break

    # Configura o 'restart'.
    while True:
        dnv = ['S', 'N']
        denovo = input('Quer jogar de novo? [S/N]: ').upper().strip()
        if denovo in dnv:
            denovo = denovo[0]
            gameover.stop()
            vitoria.stop()
            break
        print('Tente novamente.')
        tentenovamente.play()
    if denovo == 'N':
        break
    if denovo == 'S':
        confirma.play()
        pygame.mixer.music.play(-1)
        continue

encerrar.play()
print('Volte sempre!')
sleep(1.5)  # para que haja tempo de tocar o som de encerramento.
