__author__ = 'Gislaine e Izabely'


import Movimento
import Ataque
import Resistencia


class Nave(object):

    """ Uma nave posse ser usada pelo jogador ou pode ser criado para que o jogador tenha que destrui-lá
    """

    def ___init___(self):
        self._nome = "Nave"
        self._velocidade = 0
        self._dano = -1
        self._localizacao = (0, 0)
        self._movimento = Movimento.Movimento()
        self._ataque = Ataque.Ataque()
        self._resistencia = Resistencia.Resistencia()