import pygame
import constantes
import imagens
from pygame.locals import *
from sys import exit


class Botao:
    def __init__(self, x, y, largura, altura, cor_normal, cor_destaque, texto, tamanho_fonte):
        self.retangulo = pygame.Rect(x, y, largura, altura)
        self.cor_normal = cor_normal
        self.cor_destaque = cor_destaque
        self.cor_atual = cor_normal
        self.texto = texto
        self.tamanho_fonte = tamanho_fonte

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_atual, self.retangulo, 0, 10)
        fonte = pygame.font.SysFont(None, self.tamanho_fonte)
        texto = fonte.render(self.texto, True, (255, 255, 255))
        pos_texto = texto.get_rect(center=self.retangulo.center)
        tela.blit(texto, pos_texto)

    def atualizar(self, mouse_pos):
        if self.retangulo.collidepoint(mouse_pos):
            self.cor_atual = self.cor_destaque
        else:
            self.cor_atual = self.cor_normal

    def clicado(self, mouse_pos):
        return self.retangulo.collidepoint(mouse_pos)