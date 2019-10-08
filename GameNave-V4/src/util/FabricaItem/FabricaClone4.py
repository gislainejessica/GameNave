from GameNave4.src.util.FabricaItem import FabricaClone
from GameNave4.src.cgd import Path


class FabricaClone4(FabricaClone):
    def __init__(self):
        super(FabricaClone4, self).__init__(Path.get_path() + "Imagem/Item/Clone4.png")
