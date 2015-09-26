#!/usr/local/bin/python

from CamadaDominioProblema.Habilidades import Movimento
from CamadaDominioProblema.Habilidades import IA

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine
# Created:     09/19/2015
# Copyright:   (c) Gislaine Jéssica 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine'


class Municao(object):

    def __init__(self, tipoInteligente):
        self.movimento = Movimento.Movimento(tipoInteligente)
        self.figura = self.cria_figura()

    def cria_figura(self):
        self.figura = None
        return

    def movimentar(self):
        return
