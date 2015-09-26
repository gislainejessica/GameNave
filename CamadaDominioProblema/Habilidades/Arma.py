#!/usr/local/bin/python
from CamadaDominioProblema.Habilidades import Municao
# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine
# Created:     09/19/2015
# Copyright:   (c) Gislaine Jéssica 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine'


class Arma(object):
    def __init__(self):
        self.dano = None
        self.quant_municao = 1
        self.designer = None
        self.municao = Municao.Municao(1)

    def movimentar(self):
        return