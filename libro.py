from transaccion import Transaccion
from tipo import Tipo

class Libro:
    def __init__(self, isbn: str, titulo: str, precio_venta: float, precio_compra: float, cantidad_actual: int = 0, ruta_imagen: str = ""):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__precio_venta = precio_venta
        self.__precio_compra = precio_compra
        self.__cantidad_actual = cantidad_actual
        self.__ruta_imagen = ruta_imagen
        self.__transacciones = []
    
    def darIsbn(self) -> str:
        return self.__isbn

    
    def darTitulo(self) -> str:
        return self.__titulo

    
    def darPrecioVenta(self) -> float:
        return self.__precio_venta

    
    def darPrecioCompra(self) -> float:
        return self.__precio_compra

    
    def darCantidadActual(self) -> int:
        return self.__cantidad_actual

    
    def darRutaImagen(self) -> str:
        return self.__ruta_imagen

    
    def vender(self, cantidad: int, fecha: str) -> bool:  # Retorna True si la venta fue exitosa, False en caso contrario
        if cantidad <= 0:
            return False

        if self.__cantidad_actual >= cantidad:
            self.__cantidad_actual -= cantidad
            transaccion = Transaccion(Tipo.VENTA, fecha, cantidad)
            self.__transacciones.append(transaccion)
            return True
        
        return False

    
    def abastecer(self, cantidad: int, fecha: str) -> None:
        if cantidad > 0:
            self.__cantidad_actual += cantidad
            transaccion = Transaccion(Tipo.ABASTECIMIENTO, fecha, cantidad)
            self.__transacciones.append(transaccion)

    
    def darTransacciones(self):
        return self.__transacciones

    
    def toString(self) -> str:
        return f"ISBN: {self.__isbn}, Título: {self.__titulo}, Precio Venta: ${self.__precio_venta}, Precio Compra: ${self.__precio_compra}, Cantidad: {self.__cantidad_actual}"
