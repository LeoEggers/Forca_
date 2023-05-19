from random import choice
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from time import sleep


def carregar_palavras():
    with open("listas/Lista-de-Palavras.txt") as plvrs:
        fcl = []
        med = []
        dfcl = []
        for line in plvrs:
            line = line.strip()
            if 2 < len(line) <= 5:
                fcl.append(line)
            elif 5 < len(line) <= 8:
                med.append(line)
            elif len(line) > 8:
                dfcl.append(line)
        plvrs.close()
        return fcl, med, dfcl


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


def logo():
    print(
        "########################          --##########--        ####################--                @@################        --##########--")
    sleep(0.81)
    print(
        "########################      ######################    ##########################        ######################    ######################")
    sleep(0.81)
    print(
        "########################    ########################@@  ##########################      ########################  ##########################")
    sleep(0.81)
    print(
        "########################    ##########################  ############################    ########################  ##########################")
    sleep(0.81)
    print(
        "########################  ############################  ############################  @@########################  ##########################")
    sleep(0.81)
    print(
        "                                              ##########                    ##########  ##########++                                ##########++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ############################  ##########                  ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ############################  ##########                  ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ##########################MM  ##########                  ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ##########################    ##########                  ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ######################        ##########                  ##########################++")
    sleep(0.81)
    print(
        "##########                ##########--      ##########  ######################        ##########                  ##########      ##########++")
    sleep(0.81)
    print(
        "##########                ##########++      ##########  ##########  ############      ##########--                ##########      ##########++       Por LvEggers")
    sleep(0.81)
    print(
        "##########                MM##########################  ##########  @@##########      ##########################  ##########      ##########++")
    sleep(0.81)
    print(
        "##########                  ##########################  ##########    ############      ########################  ##########      ##########++")
    sleep(0.81)
    print(
        "##########                  ##########################  ##########      ##########mm    ########################  ##########      ##########++MM######################")
    sleep(0.81)
    print(
        "##########                    ######################    ##########      ############      ######################  ##########      ##########++MM######################")
    sleep(0.81)
    print(
        "##########                        ############++        ##########        ##########MM        ##################  ##########      ##########++MM######################")


def carregar_palavras_categoria(categ):
    if categ == '1':
        lista_cat = "listas/atores_atrizes.txt"
    elif categ == '2':
        lista_cat = "listas/filmes.txt"
    elif categ == '3':
        lista_cat = "listas/animais.txt"
    elif categ == '4':
        lista_cat = "listas/paises.txt"
    else:
        lista_cat = "listas/artistas_bandas.txt"

    with open(lista_cat, 'r', encoding='utf-8') as palavras_cat:
        lista_escolha = []
        for linha in palavras_cat:
            linha = linha.upper().strip()
            lista_escolha.append(linha)
        plvr = choice(lista_escolha)
        palavras_cat.close()
    return plvr


def verde(msg):
    return f'\033[1;32m{msg}\033[m'


def vermelho(msg):
    return f'\033[1;31m{msg}\033[m'


# Carrega os áudios.
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Sons/trilha.mp3')
confirma = pygame.mixer.Sound('Sons/confirma.mp3')
correto = pygame.mixer.Sound('Sons/correto.mp3')
erro = pygame.mixer.Sound('Sons/erro.mp3')
vitoria = pygame.mixer.Sound('Sons/victory.mp3')
gameover = pygame.mixer.Sound('Sons/gameover.mp3')
segredo = pygame.mixer.Sound('Sons/segredo.mp3')
tentenovamente = pygame.mixer.Sound('Sons/tentenovamente.mp3')
intro = pygame.mixer.Sound('Sons/intro.mp3')
encerrar = pygame.mixer.Sound('Sons/encerrar.mp3')

# intro.play()
# logo()

# Carrega as palavras e cria as listas das dificuldades.
facil, medio, dificil = carregar_palavras()

sleep(2)
pygame.mixer.music.play(-1)

# Lista para converter caractere para caractere acentuado automaticamente.
acento = {'A': ['Á', 'À', 'Ã', 'Â', 'Ä'],
          'E': ['É', 'Ê', 'È'],
          'I': ['Í'],
          'O': ['Ó', 'Õ', 'Ô', 'Ö'],
          'U': ['Ú'],
          'C': ['Ç']}

# Cria uma lista de emojis para erros e acertos.
emo_acerto = ['😍', '😁', '🤗', '👏', '🙌', '🤞', '☺️']
emo_erro = ['😬', '😱', '😰', '😓', '😭', '😨', '😖']

# guarda o número de vitórias consecutivas (modo 1 jogador)
cont_vit = 0
with open('melhor.txt', 'r') as arquivo_melhor:
    melhor = int(arquivo_melhor.read())  # guarda o maior número de vitórias consecutivas (modo 1 jogador)

# Início do programa.
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
            d = ['F', 'M', 'D', 'C']
            dif = input('Dificuldade[F: Fácil][M: Médio][D: Difícil][C: Por Categoria]: ').strip().upper()
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
        elif dif == 'D':
            palavra = choice(dificil)
        else:
            while True:
                cat = ['1', '2', '3', '4', '5']
                categoria = input('Escolha uma categoria: [1]Atores-Atrizes'' / '
                                  '[2]Filmes / '
                                  '[3]Animais / '
                                  '[4]Países / '
                                  '[5]Músicos-Bandas: ').strip()
                if categoria in cat:
                    categoria = categoria[0]
                    confirma.play()
                    break
                print('Tente novamente.')
                tentenovamente.play()

            palavra = carregar_palavras_categoria(categoria)

    # Cria uma sequência de underlines, um para cada letra da palavra escolhida.
    # Cria as listas tem/não tem, estabelece o número de tentativas.
    tentativas = 7
    resp = ['_' for letra in palavra]
    # Espaços não viram underline:
    for c in range(len(palavra)):
        if palavra[c] == ' ':
            resp[c] = ' '
    lista_naotem = []
    lista_tem = []

    # Começa o jogo / coleta e trata o palpite.
    cont_dica = 0
    while True:
        print(' '.join(resp))
        palpite = input('Letra: ').strip().upper()

        if not palpite.isalpha() and palpite not in ['-', ';']:
            print('Você não digitou uma letra. Tente novamente.')
            tentenovamente.play()
            continue
        else:
            palpite = palpite[0]

        # implementa substituição automática (dica)
        if palpite == ';':
            if cont_dica == 0:
                lista_dica = [c for c in range(len(resp)) if resp[c] == '_']
                subst = choice(lista_dica)
                resp[subst] = palavra[subst]
                segredo.play()
                cont_dica += 1
                continue
            else:
                print('(Já te dei uma dica...)')
                tentenovamente.play()
                continue

        if palpite in lista_tem or palpite in lista_naotem:
            print('Você já tentou essa letra!')
            tentenovamente.play()
            continue

        # Substitui caracteres sem acento por caracteres acentuados, caso existam.
        passe = False
        if palpite in acento:
            for ltr in acento[palpite]:
                if ltr in palavra:
                    passe = True
                    lista_tem.append(ltr)
                    for c in range(len(palavra)):
                        if ltr == palavra[c]:
                            resp[c] = ltr

        if palpite in palavra or passe:  # O 'passe' serve para aceitar o caractere acentuado como se fosse sem acento.
            lista_tem.append(palpite)
            correto.play()
            print(verde('Acertou!'), f'{choice(emo_acerto)}')
            for indice, letra in enumerate(palavra):
                if letra == palpite:
                    resp[indice] = palpite
            if '_' not in resp:  # Condição de vitória.
                pygame.mixer.music.stop()
                vitoria.play()
                print(' '.join(resp))
                print(verde('Parabéns! Você venceu!'), '🥳😎✨🏆🎊🎉')
                if modo == '1':
                    cont_vit += 1
                    if cont_vit > melhor:
                        melhor = cont_vit
                    with open('melhor.txt', 'w') as arquivo_melhor:
                        arquivo_melhor.write(str(melhor))  # substitui o arquivo para manter o melhor nos próximos jogos
                        arquivo_melhor.close()
                    print(f'Você ganhou {cont_vit}x consecutivamente.')
                    print(f'Melhor até agora: {melhor}')
                break
        else:
            lista_naotem.append(palpite)
            erro.play()
            print(f'{lista_naotem}')
            tentativas -= 1
            print(vermelho('Errou!'), f'{choice(emo_erro)}'
                                      f'\n Tentativas restantes: {tentativas}')
            tent(tentativas)  # Mostra a forca
            if tentativas == 0:  # Condição de derrota.
                print(vermelho('Você perdeu...'), f'☠️💔😢🥀💥 A palavra era {palavra}.')
                pygame.mixer.music.stop()
                gameover.play()
                if modo == '1':
                    print(f'Vitórias consecutivas: {cont_vit}.')
                    print(f'Melhor até agora: {melhor}')
                    cont_vit = 0
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
