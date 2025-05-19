from libro import Libro
from tipo import Tipo

class TiendaDeLibros:
    def __init__(self):
        self.__caja = 1000000
        self.__catalogo = []

    
    def darCatalogo(self):
        return self.__catalogo

    
    def darCaja(self) -> float:
        return self.__caja

    
    def cambiarCaja(self, nueva_caja: float) -> None:
        self.__caja = nueva_caja

    
    def buscarLibroPorTitulo(self, titulo: str):
        titulo_lower = titulo.lower()
        for libro in self.__catalogo:
            if libro.darTitulo().lower() == titulo_lower:
                return libro
        return None

    
    def buscarLibroPorISBN(self, isbn: str):
        for libro in self.__catalogo:
            if libro.darIsbn() == isbn:
                return libro
        return None

    
    def registrarLibro(self, isbn: str, titulo: str, precio_compra: float, precio_venta: float, ruta_imagen: str = "") -> Libro:
        for libro in self.__catalogo:
            if libro.darIsbn() == isbn:
                return ValueError(f"Ya existe un libro con el ISBN {isbn}")
        
        nuevo_libro = Libro(isbn, titulo, precio_venta, precio_compra, 0, ruta_imagen)
        self.__catalogo.append(nuevo_libro)
        return nuevo_libro

    
    def eliminarLibro(self, isbn: str) -> bool:
        for i, libro in enumerate(self.__catalogo):
            if libro.darIsbn() == isbn:
                self.__catalogo.pop(i)
                return True
        return False

    
    def abastecer(self, isbn: str, cantidad: int, fecha: str) -> bool:
        libro = self.buscarLibroPorISBN(isbn)
        if libro is None:
            return False
        
        costo_total = cantidad * libro.darPrecioCompra()
        if self.__caja >= costo_total:
            libro.abastecer(cantidad, fecha)
            self.__caja -= costo_total
            return True
        
        return False

    
    def vender(self, isbn: str, cantidad: int, fecha: str) -> bool:
        libro = self.buscarLibroPorISBN(isbn)
        if libro is None or libro.darCantidadActual() < cantidad:
            return False
        
        if libro.vender(cantidad, fecha):
            ingreso = cantidad * libro.darPrecioVenta()
            self.__caja += ingreso
            return True
        
        return False

    
    def darLibroMasCostoso(self):
        if not self.__catalogo:
            return None
        
        libro_mas_costoso = self.__catalogo[0]
        for libro in self.__catalogo[1:]:
            if libro.darPrecioVenta() > libro_mas_costoso.darPrecioVenta():
                libro_mas_costoso = libro
        
        return libro_mas_costoso

    
    def darLibroMasEconomico(self):
        if not self.__catalogo:
            return None
        
        libro_mas_economico = self.__catalogo[0]
        for libro in self.__catalogo[1:]:
            if libro.darPrecioVenta() < libro_mas_economico.darPrecioVenta():
                libro_mas_economico = libro
        
        return libro_mas_economico

    
    def darLibroMasVendido(self):
        if not self.__catalogo:
            return None
        
        libro_mas_vendido = None
        max_vendidos = 0
        
        for libro in self.__catalogo:
            total_vendidos = 0
            for transaccion in libro.darTransacciones():
                if transaccion.darTipo() == Tipo.VENTA:
                    total_vendidos += transaccion.darCantidad()
            
            if total_vendidos > max_vendidos:
                max_vendidos = total_vendidos
                libro_mas_vendido = libro
        
        return libro_mas_vendido

    
    def darCantidadTransaccionesAbastecimiento(self, isbn: str) -> int:
        libro = self.buscarLibroPorISBN(isbn)
        if libro is None:
            return 0
        
        contador = 0
        for transaccion in libro.darTransacciones():
            if transaccion.darTipo() == Tipo.ABASTECIMIENTO:
                contador += 1
        
        return contador



#metodos auxiliares segun el diagrama mostrado en clase
    
    def metodo1(self) -> str:
        return "Método 1"

    
    def metodo2(self) -> str:
        return "Método 2"
