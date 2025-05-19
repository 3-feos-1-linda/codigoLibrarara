
from transaccion import Transaccion

class Libro:
    def __init__(self, pISBN: str, pTitulo: str, pPrecioCompra: float, pPrecioVenta: float):
        self.__isbn = pISBN
        self.__titulo = pTitulo
        self.__precioCompra = pPrecioCompra
        self.__precioVenta = pPrecioVenta
        self.__cantidadActual = 0
        self.__transacciones = []
    
    
    def darISBN(self) -> str:
        return self.__isbn
    
    
    def darTitulo(self) -> str:
        return self.__titulo
    
    
    def darPrecioCompra(self) -> float:
        return self.__precioCompra
    
    
    def darPrecioVenta(self) -> float:
        return self.__precioVenta
    
    
    def darCantidadActual(self) -> int:
        return self.__cantidadActual
    
    
    def darTransacciones(self) -> list:
        return self.__transacciones
    
    
    def cambiarPrecioCompra(self, pPrecioCompra: float):
        self.__precioCompra = pPrecioCompra

    
    def cambiarPrecioVenta(self, pPrecioVenta: float):
        self.__precioVenta = pPrecioVenta

    
    def abastecer(self, pCantidad: int) -> bool:
        if pCantidad <= 0:
            return False
        
        # Crear una transacción de abastecimiento
        transaccion = Transaccion(Transaccion.Tipo.ABASTECIMIENTO, pCantidad)
        self.__transacciones.append(transaccion)
        
        # Actualizar la cantidad actual
        self.__cantidadActual += pCantidad
        return True
    
    
    def vender(self, pCantidad: int) -> bool:
        # Verificar que hay suficientes ejemplares
        if pCantidad <= 0 or pCantidad > self.__cantidadActual:
            return False
        
        # Crear una transacción de venta
        transaccion = Transaccion(Transaccion.Tipo.VENTA, pCantidad)
        self.__transacciones.append(transaccion)
        
        # Actualizar la cantidad actual
        self.__cantidadActual -= pCantidad
        return True
    

    def contarTransaccionesAbastecimiento(self) -> int:
        contador = 0
        for transaccion in self.__transacciones:
            if transaccion.darTipo() == Transaccion.Tipo.ABASTECIMIENTO:
                contador += 1
        return contador
    

    def calcularTotalVendidos(self) -> int:
        totalVendidos = 0
        for transaccion in self.__transacciones:
            if transaccion.darTipo() == Transaccion.Tipo.VENTA:
                totalVendidos += transaccion.darCantidad()
        return totalVendidos
