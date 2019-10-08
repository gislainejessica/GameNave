__author__ = 'Gislaine e Izabely'


class Item(object):

    """
    """

    def __init__(self):
        self._nome = "Item 0"
        self._modificacao = -1
        self._probabilidade = -1
        self._valor = -1

    def modifica(self):
        print("Faz algo que modifica -> Modificaçao!!!")