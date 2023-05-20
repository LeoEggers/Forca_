from random import choice
from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Funções:


def carregar_listas():
    with open("listas/Lista-de-Palavras.txt") as plvrs:
        fcl = [line.strip() for line in plvrs if 2 < len(line) <= 5]
        med = [line.strip() for line in plvrs if 5 < len(line) <= 8]
        dfcl = [line.strip() for line in plvrs if len(line) > 8]
    return fcl, med, dfcl


def carregar_listas_categoria(categ):
    caminhos = {'1': 'listas/atores_atrizes.txt',
                '2': 'listas/filmes.txt',
                '3': 'listas/animais.txt',
                '4': 'listas/paises.txt',
                '5': 'listas/artistas_bandas.txt'}

    lista_cat = caminhos.get(categ)

    with open(lista_cat, 'r', encoding='utf-8') as palavras_cat:
        lista_escolha = [linha.upper().strip() for linha in palavras_cat]
        plvr = choice(lista_escolha)
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
    # Retorna novos valores de resposta, venceu, dar_dica.
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


def resolver_acentos(palp, resp):
    # Retorna novos valores de resposta, passe.
    if palp in acento:
        for ltr in acento[palp]:
            if ltr in palavra:
                lista_tem.append(ltr)
                for c in range(len(palavra)):
                    if ltr == palavra[c]:
                        resp[c] = ltr
                        return resp, True

    return resp, False


def verificar_palpite(tent):
    if palpite in palavra or passe:  # O 'passe' serve para aceitar o caractere acentuado como se fosse sem acento.
        lista_tem.append(palpite)
        correto.play()
        print(verde('Acertou!'), f'{choice(emojis["acerto"])}')
        for indice, letra in enumerate(palavra):
            if letra == palpite:
                resposta[indice] = palpite
        if '_' not in resposta:  # Condição de vitória.
            return resposta, tent, True, False
        else:
            return resposta, tent, False, False
    else:
        lista_naotem.append(palpite)
        erro.play()
        print(f'{lista_naotem}')
        tent -= 1
        print(vermelho('Errou!'), f'{choice(emojis["erro"])}'
                                  f'\n Tentativas restantes: {tent}')
        exibir_forca(tent)  # Mostra a forca
        if tent == 0:  # Condição de derrota.
            return resposta, tent, False, True
        else:
            return resposta, tent, False, False


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
            arq_melhor.write(str(mlhr))  # Substitui o arquivo para manter o melhor nos próximos jogos.
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

# Guarda o número de vitórias consecutivas (modo 1 jogador).
cont_vit = 0
with open('melhor.txt', 'r') as arquivo_melhor:
    melhor = int(arquivo_melhor.read())  # Guarda o maior número de vitórias consecutivas (modo 1 jogador).

# Início do programa.
while True:
    # Variáveis mutáveis:
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
        resposta, passe = resolver_acentos(palpite, resposta)

        # Verifica se o palpite está na palavra.
        resposta, tentativas, venceu, perdeu = verificar_palpite(tentativas)

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
