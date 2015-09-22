#!/usr/local/bin/python
from CamadaDominioProblema.Veiculo import Inimigo

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine
# Created:     09/19/2015
# Copyright:   (c) Gislaine Jéssica 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine'


class General(Inimigo):
    def __init__(self, nome, figura):
        super.__init__(nome, figura)