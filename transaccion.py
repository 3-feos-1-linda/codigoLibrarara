from enum import Enum

class Transaccion:
    
    class Tipo(Enum):
        VENTA = 1
        ABASTECIMIENTO = 2
    

    def __init__(self, pTipo: Tipo, pCantidad: int):
        self.__tipo = pTipo
        self.__fecha = "Fecha actual" 
        self.__cantidad = pCantidad
    

    def darTipo(self):
        return self.__tipo
    

    def darFecha(self):
        return self.__fecha
    
    
    def darCantidad(self):
        return self.__cantidad