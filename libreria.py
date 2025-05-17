from libro import Libro

class Libreria:
    
    def __init__(self):
        self.__catalogo = []  # Lista de libros en el catálogo
        self.__dineroEnCaja = 1000000  # Inversión inicial de $1.000.000
    
    def darCatalogo(self) -> list:
        return self.__catalogo
    
    def darDineroEnCaja(self) -> float:
        return self.__dineroEnCaja
    
    def registrarLibro(self, pISBN: str, pTitulo: str, pPrecioCompra: float, pPrecioVenta: float) -> bool:
        # Verificar que no exista otro libro con el mismo ISBN
        for libro in self.__catalogo:
            if libro.darISBN() == pISBN:
                return False
        
        # Crear y agregar un nuevo libro al catálogo
        nuevoLibro = Libro(pISBN, pTitulo, pPrecioCompra, pPrecioVenta)
        self.__catalogo.append(nuevoLibro)
        return True
    
    def eliminarLibro(self, pISBN: str) -> bool:
        for i, libro in enumerate(self.__catalogo):
            if libro.darISBN() == pISBN:
                del self.__catalogo[i]
                return True
        return False
    
    def buscarLibroPorTitulo(self, pTitulo: str) -> Libro:
        for libro in self.__catalogo:
            if libro.darTitulo() == pTitulo:
                return libro
        return None
    
    def buscarLibroPorISBN(self, pISBN: str) -> Libro:
        for libro in self.__catalogo:
            if libro.darISBN() == pISBN:
                return libro
        return None
    
    def abastecerLibro(self, pISBN: str, pCantidad: int) -> bool:
        libro = self.buscarLibroPorISBN(pISBN)
        if libro is None:
            return False
        
        # Calcular costo total de abastecimiento
        costoTotal = libro.darPrecioCompra() * pCantidad
        
        # Verificar si hay suficiente dinero en caja
        if costoTotal > self.__dineroEnCaja:
            return False
        
        # Realizar el abastecimiento
        if libro.abastecer(pCantidad):
            self.__dineroEnCaja -= costoTotal
            return True
        
        return False
    
    def venderLibro(self, pISBN: str, pCantidad: int) -> bool:
        libro = self.buscarLibroPorISBN(pISBN)
        if libro is None:
            return False
        
        # Realizar la venta
        if libro.vender(pCantidad):
            # Actualizar el dinero en caja
            ingresoTotal = libro.darPrecioVenta() * pCantidad
            self.__dineroEnCaja += ingresoTotal
            return True
        
        return False
    
    def contarTransaccionesAbastecimientoLibro(self, pISBN: str) -> int:
        libro = self.buscarLibroPorISBN(pISBN)
        if libro is None:
            return -1
        
        return libro.contarTransaccionesAbastecimiento()
    
    def buscarLibroMasCostoso(self) -> Libro:
        if not self.__catalogo:
            return None
        
        libroMasCostoso = self.__catalogo[0]
        for libro in self.__catalogo:
            if libro.darPrecioVenta() > libroMasCostoso.darPrecioVenta():
                libroMasCostoso = libro
        
        return libroMasCostoso
    
    def buscarLibroMenosCostoso(self) -> Libro:
        if not self.__catalogo:
            return None
        
        libroMenosCostoso = self.__catalogo[0]
        for libro in self.__catalogo:
            if libro.darPrecioVenta() < libroMenosCostoso.darPrecioVenta():
                libroMenosCostoso = libro
        
        return libroMenosCostoso
    
    def buscarLibroMasVendido(self) -> Libro:
        if not self.__catalogo:
            return None
        
        libroMasVendido = None
        maxVentas = -1
        
        for libro in self.__catalogo:
            ventasLibro = libro.calcularTotalVendidos()
            if ventasLibro > maxVentas:
                maxVentas = ventasLibro
                libroMasVendido = libro
        
        return libroMasVendido
