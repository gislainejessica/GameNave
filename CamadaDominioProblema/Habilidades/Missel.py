#!/usr/local/bin/python
from CamadaDominioProblema.Habilidades import Ataque

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine
# Created:     09/19/2015
# Copyright:   (c) Gislaine Jéssica 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine'


class Missel(Ataque):

    def __init__(self):
        self.super.__init__()
        self.manipulacao = 0
        self.figura = None

    def atirar (self):
        self.figura = 0  #
        return self.figura
