from tipo import Tipo

class Transaccion:
    def __init__(self, tipo: Tipo, fecha: str, cantidad: int):
        self.__tipo = tipo
        self.__fecha = fecha
        self.__cantidad = cantidad
    
    def darTipo(self) -> Tipo:
        return self.__tipo
        
    def darFecha(self) -> str:
        return self.__fecha
        
    def darCantidad(self) -> int:
        return self.__cantidad
    
    def toString(self) -> str:  #aparece en el diagrama mostrado en clase, devuelve una representación en cadena de la transacción.
        tipo_str = "Venta" if self.__tipo == Tipo.VENTA else "Abastecimiento"
        return f"{tipo_str} - Fecha: {self.__fecha} - Cantidad: {self.__cantidad}"
