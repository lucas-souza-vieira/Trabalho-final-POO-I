import pygame
import random
import constantes
from botoes import Botao
from pygame.locals import *
from sys import exit

timer = pygame.time.Clock()

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("audios/8bit Bossa.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    global botoes_som
    botoes_som  = pygame.mixer.Sound("audios/botoes.wav")
    botoes_som.set_volume(0.1)
    
    tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
    pygame.display.set_caption(constantes.TITULO)
    rodando = True

    global numeros_possiveis
    global numero_aleatorio
    global vetor
    numeros_possiveis = list(range(2, 12))
    numero_aleatorio = random.choice(numeros_possiveis) 
    numeros_possiveis.remove(numero_aleatorio)
    vetor = dicionario[numero_aleatorio]

    usado = False
    usado2 = False


    botoes_menu = [
        Botao(550, 620, 400, 100, (254, 208, 66), (204, 169, 60), "Jogar", 70),
        Botao(980, 620, 400, 100, (254, 208, 66), (204, 169, 60), "Créditos", 70),
        Botao(865, 770, 200, 50, (254, 208, 66), (204, 169, 60), "Sair", 70)
    ]

    mouse_pos = (0, 0)
    tela_atual = "menu"

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for botao in botoes_menu:
                    if botao.clicado(mouse_pos):
                        if botao.texto == "Jogar":
                            botoes_som.play()
                            tela_atual = exibir_tela_jogo(tela, mouse_pos, vetor, pontos, usado, usado2)
                        elif botao.texto == "Créditos":
                            botoes_som.play()
                            tela_atual = exibir_tela_creditos(tela, mouse_pos)
                        elif botao.texto == "Sair":
                            botoes_som.play()
                            rodando = False

        if tela_atual == "menu":
            mouse_pos = pygame.mouse.get_pos()
            for botao in botoes_menu:
                botao.atualizar(mouse_pos)
        

        tela_atual = menu(tela, botoes_menu, mouse_pos)

        pygame.display.flip()

    pygame.quit()


def menu(tela, botoes, mouse_pos):
    tela_atual = "menu"

    imagem_fundo = pygame.image.load("imagens/backdrop.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1920, 1080))

    logo_ufsc = pygame.image.load("imagens/logoUFSC.png")
    logo_ufsc = pygame.transform.scale(logo_ufsc, (160, 160))

    logo_jogo = pygame.image.load("imagens/logo_jogo.png")
    logo_jogo = pygame.transform.scale(logo_jogo, (1280, 720))

    tela.blit(imagem_fundo, (0, 0))
    tela.blit(logo_ufsc, (880, 30))
    tela.blit(logo_jogo, (370, 50))

    for botao in botoes:
        botao.desenhar(tela)

    return tela_atual


def exibir_tela_creditos(tela, mouse_pos):
    tela_atual = "creditos"
    

    imagem_fundo = pygame.image.load("imagens/backdrop.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1920, 1080))

    botao_voltar = Botao(15, 15, 200, 50, (254, 208, 66), (204, 169, 60), "(<) voltar", 40)

    fonte = pygame.font.SysFont(None, 250)
    fonte2 = pygame.font.SysFont(None, 60)
    texto1 = fonte.render("Créditos:", True, (255, 255, 255))
    texto2 = fonte2.render("Trabalho de Programação Orientada a Objetos", True, (255, 255, 255))
    texto3 = fonte2.render("Alunos: Lucas de Souza Vieira e Tom Hunt", True, (255, 255, 255))
    texto4 = fonte2.render("Professor: Maicon Zatelli", True, (255, 255, 255))
    texto5 = fonte2.render("Sons de domínio público utilizados dos seguintes sites:", True, (255, 255, 255) )
    texto6 = fonte2.render("https://opengameart.org/content/bossa-nova", True, (255, 255, 255))
    texto7 = fonte2.render("https://mixkit.co", True, (255, 255, 255))


    while tela_atual == "creditos":
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao_voltar.clicado(mouse_pos):
                    botoes_som.play()
                    tela_atual = "menu"
            mouse_pos = pygame.mouse.get_pos()


        botao_voltar.atualizar(mouse_pos)
        tela.blit(imagem_fundo, (0, 0))
        tela.blit(texto1, (570, 170))
        tela.blit(texto2, (490, 440))
        tela.blit(texto3, (527, 540))
        tela.blit(texto4, (705, 640))
        tela.blit(texto5, (400, 780))
        tela.blit(texto6, (500, 830))
        tela.blit(texto7, (785, 880))

        botao_voltar.desenhar(tela)
        pygame.display.flip()

    return tela_atual

dicionario = {
    1 : ["pgt", "a", "b", "c", "d", "colegas", "professores", "gpt", 0], 
    2 : ["Quantos campus a UFSC possui e em que cidades eles estão?", "A) 6 campus - Florianópolis, Joinville, Blumenau, Curitibanos, Araranguá.", "B) 5 campus - Florianópolis, Joinville, Blumenau, Curitibanos, Araranguá.", "C) 4 campus - Florianópolis, Joinville, Blumenau, Araranguá.", "D) 3 campus - Florianópolis, Joinville, Araranguá.", "A"], 
    3 : ["Em que ano a UFSC foi fundada?", "A) 1950.", "B) 1960.", "C) 1970.", "D) 1968.", "B"],
    4 : ["Qual o atual reitor da UFSC?", "A) Ubaldo Cesar Balthazar.", "B) João David Ferreira Lima.", "C) Irineu Manoel de Souza.", "D) Luiz Carlos Cancellier de Olivo.", "C"],
    5 : ["Qual o nome da festa de computação?", "A) Amnésia.", "B) Apocalipse.", "C) Calourada.", "D) Computaria.", "A"],
    6 : ["Quantos cursos de graduação a UFSC tem?", "A) 138.", "B) 120.", "C) 89.", "D) 99.", "D"],
    7 : ["O que é um loop em Python?", "A) Um loop em Python é uma função de impressão.", "B) Uma estrutura de controle para repetir um bloco de código.", "C) Um loop em Python é uma instrução condicional.", "D) Um loop em Python é uma variável de armazenamento.", "B"], 
    8 : ["Diferença entre listas e tuplas em Python?", "A) Listas e tuplas são a mesma coisa em Python.", "B) Listas são imutáveis, tuplas são mutáveis.", "C) Listas são mutáveis, tuplas são imutáveis", "D) Listas são usadas para armazenar números, tuplas para armazenar strings.", "C"],
    9 : ["Para que serve o módulo random em Python?", "A) É usado para criar animações em 3D.", "B) É usado para realizar cálculos matriciais.", "C) É usado para manipular arquivos de texto.", "D) Geração de números aleatórios.", "D"],
    10 : ["Qual função verifica o tipo de uma variável em Python?", "A) var_type().", "B) typeof().", "C) check().", "D) type().", "D"],
    11 : ["Qual é o nome da função condicional?", "A) If-else.", "B) While.", "C) For.", "D) Matriz.", "A"]
}

numeros_possiveis = list(range(2, 12))
numero_aleatorio = random.choice(numeros_possiveis)  
numeros_possiveis.remove(numero_aleatorio)  
vetor = dicionario[numero_aleatorio]
pontos = 0

def transicao():
    numero_aleatorio = random.choice(numeros_possiveis) 
    numeros_possiveis.remove(numero_aleatorio)
    vetor = dicionario[numero_aleatorio]
    return vetor



def exibir_tela_jogo(tela, mouse_pos, vetor, pontos, usado, usado2):
    tela_atual = "jogo"
    
    imagem_fundo = pygame.image.load("imagens/backdrop.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1920, 1080))

    
    botao_desistir = Botao(70, 935, 200, 75, (153, 1, 0), (82, 16, 4), "(X) Desistir", 40)
    botao_pgt = Botao(70, 50, 1780, 200, (254, 208, 66), (204, 169, 60), vetor[0], 70)
    botao_a = Botao(70, 300, 1300, 100, (254, 208, 66), (204, 169, 60), vetor[1], 40)
    botao_b = Botao(70, 450, 1300, 100, (254, 208, 66), (204, 169, 60), vetor[2], 40)
    botao_c = Botao(70, 600, 1300, 100, (254, 208, 66), (204, 169, 60), vetor[3], 40)
    botao_d = Botao(70, 750, 1300, 100, (254, 208, 66), (204, 169, 60), vetor[4], 40)
    botao_pontos = Botao(1650, 935, 200, 75, (254, 208, 66), (204, 169, 60), f'Pontos: {pontos}', 40)

    gpt = Botao(1420, 300, 430, 250, (25, 195, 125), (64, 92, 80), "Chat GPT", 40)
    card = Botao(600, 200, 800, 800, (25, 195, 125), (255, 0, 0), f'A resposta certa é: {vetor[5]}', 40)

    vetor_colega = ["A", "B", "C", "D"]
    vetor_colega.remove(vetor[5])
    print(vetor_colega)
    resposta_errada = random.choice(vetor_colega)


    colega = Botao(1420, 600, 430, 250, (198, 81, 2), (82, 16, 4), "Colega", 40)
    card2 = Botao(600, 200, 800, 800, (198, 81, 2), (255, 0, 0), f'A resposta certa é: {resposta_errada}', 40)


    card_aberto = False
    card2_aberto = False

       
    certa = pygame.mixer.Sound("audios/certa.wav")
    errada = pygame.mixer.Sound("audios/errada.wav")
    certa.set_volume(0.1)
    errada.set_volume(0.1)
        
    while tela_atual == "jogo":
        timer.tick(60)
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if not usado:
                    if gpt.clicado(mouse_pos):
                        card_aberto = not card_aberto
                        if (not card_aberto) & (not usado):
                            usado = True
                        
                if not usado2:
                    if colega.clicado(mouse_pos):
                        card2_aberto = not card2_aberto
                        if (not card2_aberto) & (not usado2):
                            usado2 = True
                
                if botao_desistir.clicado(mouse_pos):
                    botoes_som.play()
                    tela_atual = main()

                if card_aberto:
                    continue
                elif card2_aberto:
                    continue
                else:
                    if botao_a.clicado(mouse_pos):
                        resposta = "A"
                        if resposta == vetor[5]:
                            pontos += 1
                            certa.play()
                        else:
                            errada.play()
                        if (len(numeros_possiveis) == 0):
                            tela_atual = exibir_tela_final(tela, mouse_pos, pontos)
                        else:
                            vetor = transicao()
                        tela_atual = exibir_tela_jogo(tela, mouse_pos, vetor, pontos, usado, usado2)

                    if botao_b.clicado(mouse_pos):
                        resposta = "B"
                        if resposta == vetor[5]:
                            pontos += 1
                            certa.play()
                        else:
                            errada.play()
                        if (len(numeros_possiveis) == 0):
                            tela_atual = exibir_tela_final(tela, mouse_pos, pontos)
                        else:
                            vetor = transicao()
                        tela_atual = exibir_tela_jogo(tela, mouse_pos, vetor, pontos, usado, usado2)

                    if botao_c.clicado(mouse_pos):
                        resposta = "C"
                        if resposta == vetor[5]:
                            pontos += 1
                            certa.play()
                        else:
                            errada.play()
                        if (len(numeros_possiveis) == 0):
                            tela_atual = exibir_tela_final(tela, mouse_pos, pontos)
                        else:
                            vetor = transicao()
                        tela_atual = exibir_tela_jogo(tela, mouse_pos, vetor, pontos, usado, usado2)

                    if botao_d.clicado(mouse_pos):
                        resposta = "D"
                        if resposta == vetor[5]:
                            pontos += 1
                            certa.play()
                        else:
                            errada.play()
                        if (len(numeros_possiveis) == 0):
                            tela_atual = exibir_tela_final(tela, mouse_pos, pontos)
                        else:
                            vetor = transicao()
                        tela_atual = exibir_tela_jogo(tela, mouse_pos, vetor, pontos, usado, usado2)        

            mouse_pos = pygame.mouse.get_pos()
            

        tela.blit(imagem_fundo, (0, 0))
        botao_desistir.atualizar(mouse_pos)
        gpt.atualizar(mouse_pos)
        colega.atualizar(mouse_pos) 

    
        if card_aberto:
            if not usado:
                gpt.atualizar(mouse_pos)
        elif card2_aberto:
            if not usado2:
                colega.atualizar(mouse_pos) 
        else:
            botao_a.atualizar(mouse_pos)
            botao_b.atualizar(mouse_pos)
            botao_c.atualizar(mouse_pos)
            botao_d.atualizar(mouse_pos)



        botao_desistir.desenhar(tela)
        botao_pgt.desenhar(tela)
        botao_a.desenhar(tela)
        botao_b.desenhar(tela)
        botao_c.desenhar(tela)
        botao_d.desenhar(tela)
        botao_pontos.desenhar(tela)
        gpt.desenhar(tela)
        colega.desenhar(tela)

        if card_aberto == True:
            card.desenhar(tela)
        
        if card2_aberto == True:
            card2.desenhar(tela)

        if usado:
            gpt = Botao(1420, 300, 430, 250, (64, 92, 80), (64, 92, 80), "Chat GPT", 40)
        
        if usado2:
            colega = Botao(1420, 600, 430, 250, (82, 16, 4), (82, 16, 4), "Colega", 40)

        
        

        pygame.display.flip()


    return tela_atual

def exibir_tela_final(tela, mouse_pos, pontos):
    tela_atual = "final"

    imagem_fundo = pygame.image.load("imagens/backdrop.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1920, 1080))
    botao_replay = Botao(785, 505, 350, 70, (254, 208, 66), (204, 169, 60), "Jogar de novo", 60)


    pygame.mixer.music.stop()
    winner = pygame.mixer.Sound("audios/winner.wav")
    lose  = pygame.mixer.Sound("audios/lose.wav")

    if pontos >= 6:
        winner.play()
    else:
        lose.play()
    


    while tela_atual == "final":
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao_replay.clicado(mouse_pos):
                    botoes_som.play()
                    tela_atual = main()
            mouse_pos = pygame.mouse.get_pos()
        mouse_pos = pygame.mouse.get_pos()

        tela.blit(imagem_fundo, (0, 0))
        botao_replay.atualizar(mouse_pos)
        botao_replay.desenhar(tela)
        if pontos >= 6:
            fonte = pygame.font.SysFont("None", 110)
            textoa = fonte.render("Parabéns, você foi aprovado!", True, (255, 255, 255))
            tela.blit(textoa, (410, 250))
        else:
            fonte = pygame.font.SysFont("None", 110)
            textob = fonte.render("Infelizmente, você foi reprovado.", True, (255, 255, 255))
            tela.blit(textob, (345,250))

        texto_nota = fonte.render(f"Com nota {pontos}.", True, (255,255,255))
        tela.blit(texto_nota, (745,350))

        pygame.display.flip()


    return tela_atual

    
main()