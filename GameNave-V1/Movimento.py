__author__ = 'Gislaine e Izabely'


class Movimento(object):

    """ Existem varios tipos de movimentos dependendo do tipo de nave.
    """

    def __init__(self):
        self._estrategia = -1
        self._nome = "Movimento 0"
        self._direcoes = [1, 2, 3, 4]
        self._definicao = -1
