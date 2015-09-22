#!/usr/local/bin/python
import pygame
from pygame.locals import *
from CamadaDominioProblema.Veiculo import Nave

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine
# Created:     09/19/2015
# Copyright:   (c) Gislaine Jéssica 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine'


class Jogador(Nave):

    def __init__(self, nome, figura):
        super.__init__(nome, figura)
        self.fase = 0
        self.pontuacao = 0
        self.tempoMissel = 0

    @staticmethod
    def start_controles():

        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

        return pygame.mixer.Sound("/home/gislaine/Dropbox/GameNave/CamadaGestaoDados/Som/MusicNave.wav")

    def get_area(self):

        return self.area

    @staticmethod
    def start_figura(figura):

        f = pygame.image.load(figura).convert_alpha()

        return f

    def start_area(self):

        self.area = Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())

        return Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())

    def buzina(self):

        self.som.set_volume(0.1)
        self.som.play()
