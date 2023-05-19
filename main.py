from random import choice
from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Funções:


def carregar_listas():
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


def carregar_listas_categoria(categ):
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


def num_jogadores():
    while True:
        md = ['1', '2']
        num_jog = input('Escolha o número de jogadores [1/2]: ').strip()
        if num_jog in md:
            confirma.play()
            break
        print('Tente novamente.')
        tentenovamente.play()
    return num_jog[0]


def carregar_palavra():
    # Modo 2 jogadores: um dos jogadores escolhe a palavra.
    if modo == '2':
        plvr = input('Escolha uma palavra: ').strip().upper()
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
            plvr = choice(facil)
        elif dif == 'M':
            plvr = choice(medio)
        elif dif == 'D':
            plvr = choice(dificil)
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

            plvr = carregar_listas_categoria(categoria)

    return plvr


def coletar_palpite():
    while True:
        plpt = input('Letra: ').strip().upper()

        if not plpt.isalpha() and plpt not in ['-', ';']:
            print('Você não digitou uma letra. Tente novamente.')
            tentenovamente.play()
        else:
            return plpt[0]


def exibir_forca(t):
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


def exibir_logo():
    print(
        "########################          --##########--        ####################--                "
        "@@################        --##########--")
    sleep(0.81)
    print(
        "########################      ######################    ##########################        "
        "######################    ######################")
    sleep(0.81)
    print(
        "########################    ########################@@  ##########################      "
        "########################  ##########################")
    sleep(0.81)
    print(
        "########################    ##########################  ############################    "
        "########################  ##########################")
    sleep(0.81)
    print(
        "########################  ############################  ############################  "
        "@@########################  ##########################")
    sleep(0.81)
    print(
        "##########                    ##########  ##########++                                ##########++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ############################  ##########             "
        "     ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ############################  ##########             "
        "     ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ##########################MM  ##########             "
        "     ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ##########################    ##########             "
        "     ##########################++")
    sleep(0.81)
    print(
        "########################  ##########--      ##########  ######################        ##########             "
        "     ##########################++")
    sleep(0.81)
    print(
        "##########                ##########--      ##########  ######################        ##########             "
        "     ##########      ##########++")
    sleep(0.81)
    print(
        "##########                ##########++      ##########  ##########  ############      ##########--           "
        "     ##########      ##########++       Por LvEggers")
    sleep(0.81)
    print(
        "##########                MM##########################  ##########  @@##########      "
        "##########################  ##########      ##########++")
    sleep(0.81)
    print(
        "##########                  ##########################  ##########    ############      "
        "########################  ##########      ##########++")
    sleep(0.81)
    print(
        "##########                  ##########################  ##########      ##########mm    "
        "########################  ##########      ##########++MM######################")
    sleep(0.81)
    print(
        "##########                    ######################    ##########      ############      "
        "######################  ##########      ##########++MM######################")
    sleep(0.81)
    print(
        "##########                        ############++        ##########        ##########MM        "
        "##################  ##########      ##########++MM######################")


def resolver_dica(resp, plvr, dar_dic):
    # retorna novos valores de resposta, venceu, dar_dica.
    if dar_dic:
        lista_dica = [n for n in range(len(resp)) if resp[n] == '_']
        subst = choice(lista_dica)
        resp[subst] = plvr[subst]
        segredo.play()
        if '_' not in resposta:
            return resp, True, False
    else:
        print('(Já te dei uma dica...)')
        tentenovamente.play()

    return resp, False, False


def vencer(mod, cont_v, mlhr):
    pygame.mixer.music.stop()
    vitoria.play()
    print(' '.join(resposta))
    print(verde('Parabéns! Você venceu!'), '🥳😎✨🏆🎊🎉')
    if mod == '1':
        cont_v += 1
        if cont_v > mlhr:
            mlhr = cont_v
        with open('melhor.txt', 'w') as arq_melhor:
            arq_melhor.write(str(mlhr))  # substitui o arquivo para manter o melhor nos próximos jogos
            arq_melhor.close()
        print(f'Você ganhou {cont_v}x consecutivamente.')
        print(f'Melhor até agora: {mlhr}')
        return cont_v


def perder(mod, cont_v):
    print(vermelho('Você perdeu...'), f'☠️💔😢🥀💥 A palavra era {palavra}.')
    pygame.mixer.music.stop()
    gameover.play()
    if mod == '1':
        print(f'Vitórias consecutivas: {cont_v}.')
        with open('melhor.txt', 'r') as arq_melhor:
            mlhr = arq_melhor.read()
            arq_melhor.close()
        print(f'Melhor até agora: {mlhr}')
        cont_v = 0
    return cont_v


def verde(msg):
    return f'\033[1;32m{msg}\033[m'


def vermelho(msg):
    return f'\033[1;31m{msg}\033[m'


# Áudios.
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

# Introdução.
intro.play()
exibir_logo()
sleep(2)
pygame.mixer.music.play(-1)

# Carrega as palavras e cria as listas das dificuldades.
facil, medio, dificil = carregar_listas()

# Dicionário para converter caractere para caractere acentuado automaticamente.
acento = {'A': ['Á', 'À', 'Ã', 'Â', 'Ä'],
          'E': ['É', 'Ê', 'È'],
          'I': ['Í'],
          'O': ['Ó', 'Õ', 'Ô', 'Ö'],
          'U': ['Ú'],
          'C': ['Ç']}

# Dicionário de emojis para erros e acertos.
emojis = {'acerto': ['😍', '😁', '🤗', '👏', '🙌', '🤞', '☺️'],
          'erro': ['😬', '😱', '😰', '😓', '😭', '😨', '😖']}

# guarda o número de vitórias consecutivas (modo 1 jogador)
cont_vit = 0
with open('melhor.txt', 'r') as arquivo_melhor:
    melhor = int(arquivo_melhor.read())  # guarda o maior número de vitórias consecutivas (modo 1 jogador)

# Início do programa.
while True:
    # variáveis mutáveis:
    tentativas = 7
    dar_dica = True
    lista_naotem = []
    lista_tem = []
    perdeu = False
    venceu = False

    # Escolhe o número de jogadores.
    modo = num_jogadores()

    # Carrega a palavra.
    palavra = carregar_palavra()

    # Cria underlines para cada letra da palavra selecionada, ignorando os espaços.
    resposta = [' ' if letra == ' ' else '_' for letra in palavra]

    # Começa o jogo.
    while True:

        # Confere os booleans "venceu"/"perdeu".
        if venceu:
            cont_vit = vencer(modo, cont_vit, melhor)
            break

        if perdeu:
            cont_vit = perder(modo, cont_vit)
            break

        print(' '.join(resposta))

        # Coleta e trata o palpite.
        palpite = coletar_palpite()

        # Resolve o pedido por dica (substituição automática).
        if palpite == ';':
            resposta, venceu, dar_dica = resolver_dica(resposta, palavra, dar_dica)
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
                            resposta[c] = ltr

        # Verifica se o palpite está na palavra.
        if palpite in palavra or passe:  # O 'passe' serve para aceitar o caractere acentuado como se fosse sem acento.
            lista_tem.append(palpite)
            correto.play()
            print(verde('Acertou!'), f'{choice(emojis["acerto"])}')
            for indice, letra in enumerate(palavra):
                if letra == palpite:
                    resposta[indice] = palpite
            if '_' not in resposta:  # Condição de vitória.
                venceu = True
        else:
            lista_naotem.append(palpite)
            erro.play()
            print(f'{lista_naotem}')
            tentativas -= 1
            print(vermelho('Errou!'), f'{choice(emojis["erro"])}'
                                      f'\n Tentativas restantes: {tentativas}')
            exibir_forca(tentativas)  # Mostra a forca
            if tentativas == 0:  # Condição de derrota.
                perdeu = True

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
    else:
        confirma.play()
        pygame.mixer.music.play(-1)
        continue

# Fim.
encerrar.play()
print('Volte sempre!')
sleep(1.5)  # Para que haja tempo de tocar o som de encerramento.
