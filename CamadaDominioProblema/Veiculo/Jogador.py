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
        super(nome, figura)
        self.fase = 0
        self.pontuacao = 0
        self.tempoMissel = 0

