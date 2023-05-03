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


# Carregando os áudios.
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

# Carregando as palavras e criando as listas das dificuldades.
palavras = open("Lista-de-Palavras.txt")
facil = []
medio = []
dificil = []

# Lista para converter caractere para caractere acentuado automaticamente.
# acento = {'A': ['Á', 'Ã', 'Â'], 'E': ['É', 'Ê'], 'I': ['Í'], 'O': ['Ó', 'Õ', 'Ô'], 'U': ['Ú'], 'C': ['Ç']}

# Criando uma lista de emojis para erros e acertos.
emo_acerto = ['😍', '😁', '🤗', '👏', '🙌', '🤞', '☺️']
emo_erro = ['😬', '😱', '😰', '😓', '😭', '😨', '😖']

# carregando a lista das dificuldades por extensão.
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

    tentativas = 7
    resp = ['_' for letra in palavra]
    lista_naotem = []
    lista_tem = []

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

        if palpite in palavra:
            lista_tem.append(palpite)
            correto.play()
            print(f'\033[1;32mAcertou!\033[m {choice(emo_acerto)}')
            # OBS.: Este trecho ainda não tem necessidade, pois a lista de palavras
            # não possui palavras com acento ou cedilhas, mas caso isso mude futuramente
            # uma função que substitui automaticamente um caractere para o caractere
            # acentuado já está implementada.
            #
            # if palpite in acento.keys():
            #     for ltr in acento[palpite]:
            #         if ltr in palavra:
            #             resp[palavra.index(ltr)] = ltr
            for indice, letra in enumerate(palavra):
                if letra == palpite:
                    resp[indice] = palpite
            if '_' not in resp:
                pygame.mixer.music.stop()
                vitoria.play()
                print(' '.join(resp))
                print('\033[1;32mParabéns! Você venceu!\033[m 🥳😎✨🏆🎊🎉')
                break
        else:
            lista_naotem.append(palpite)
            erro.play()
            print(f'{lista_naotem}')
            tentativas -= 1
            print(f'\033[1;31mErrou!\033[m {choice(emo_erro)}'
                  f'\n Tentativas restantes: {tentativas}')
            tent(tentativas)
            if tentativas == 0:
                print(f'\033[1;31mVocê perdeu...\033[m ☠️💔😢🥀💥 A palavra era {palavra}.')
                pygame.mixer.music.stop()
                gameover.play()
                break

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
