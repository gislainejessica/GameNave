__author__ = 'Gislaine e Izabely'

import Nave
import Item


class NaveCombatente(Nave):

    """ Nave que será usada pelo jogador no jogo.
    """

    def __init__(self):
        self._id = -1
        self._pontuacao = 0
        self._timeMissel = 0
        self._itens = [Item.Item()]