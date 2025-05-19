from TiendaDeLibros import TiendaDeLibros
from libro import Libro
from transaccion import Transaccion
from tipo import Tipo
import datetime

def obtener_fecha_actual() -> str:
    hoy = datetime.datetime.now()
    return hoy.strftime("%d/%m/%Y")


def main():
    print("<<< SISTEMA DE TIENDA DE LIBROS >>>\n")
    
    tienda = TiendaDeLibros()
    print(f"Caja inicial: ${tienda.darCaja():.2f}\n")
    
    # Registro de algunos libros
    try:
        libro1 = tienda.registrarLibro("9789584276148", "Cien años de soledad", 30000, 45000)
        print(f"Libro registrado: {libro1.toString()}")
        
        libro2 = tienda.registrarLibro("9788498387087", "El Principito", 15000, 25000)
        print(f"Libro registrado: {libro2.toString()}")
                                      
        libro3 = tienda.registrarLibro("9788498383621", "En esta noche, en este mundo", 25000, 38000)
        print(f"Libro registrado: {libro3.toString()}")
        
        print("\nCatálogo actual:")
        for libro in tienda.darCatalogo():
            print(f"- {libro.toString()}")
    except ValueError as e:
        print(f"Error: {e}")

    
    # Abastecer libros
    fecha_actual = obtener_fecha_actual()
    print("\n=== ABASTECIMIENTO DE LIBROS ===")
    

    if tienda.abastecer("9789584276148", 10, fecha_actual):
        print(f"Se abasteció 'Cien años de soledad' con 10 ejemplares. Caja: ${tienda.darCaja():.2f}")
    else:
        print("No se pudo abastecer 'Cien años de soledad'")
    
    if tienda.abastecer("9788498387087", 15, fecha_actual):
        print(f"Se abasteció 'El Principito' con 15 ejemplares. Caja: ${tienda.darCaja():.2f}")
    else:
        print("No se pudo abastecer 'El Principito'")
    
    if tienda.abastecer("9788498383621", 8, fecha_actual):
        print(f"Se abasteció 'En esta noche, en este mundo' con 8 ejemplares. Caja: ${tienda.darCaja():.2f}")
    else:
        print("No se pudo abastecer 'En esta noche, en este mundo'")

    
    # Vender libros
    print("\n=== VENTA DE LIBROS ===")
    

    if tienda.vender("9789584276148", 3, fecha_actual):
        print(f"Se vendieron 3 ejemplares de 'Cien años de soledad'. Caja: ${tienda.darCaja():.2f}")
    else:
        print("No se pudo realizar la venta de 'Cien años de soledad'")
    
    if tienda.vender("9788498387087", 7, fecha_actual):
        print(f"Se vendieron 7 ejemplares de 'El Principito'. Caja: ${tienda.darCaja():.2f}")
    else:
        print("No se pudo realizar la venta de 'El Principito'")
    
    # Intentar vender más ejemplares de los disponibles, error
    if tienda.vender("9788498383621", 10, fecha_actual):
        print(f"Se vendieron 10 ejemplares de 'En esta noche, en este mundo'. Caja: ${tienda.darCaja():.2f}")
    else:
        print("No se pudo realizar la venta de 'En esta noche, en este mundo' (stock insuficiente)")

    
    # Buscar libros
    print("\n=== BÚSQUEDA DE LIBROS ===")
    
    # por título
    titulo_buscar = "El Principito"
    libro_encontrado = tienda.buscarLibroPorTitulo(titulo_buscar)
    if libro_encontrado:
        print(f"Libro encontrado por título '{titulo_buscar}': {libro_encontrado.toString()}")
    else:
        print(f"No se encontró ningún libro con título '{titulo_buscar}'")
    
    # por ISBN
    isbn_buscar = "9788498383621"
    libro_encontrado = tienda.buscarLibroPorISBN(isbn_buscar)
    if libro_encontrado:
        print(f"Libro encontrado por ISBN '{isbn_buscar}': {libro_encontrado.toString()}")
    else:
        print(f"No se encontró ningún libro con ISBN '{isbn_buscar}'")
        
    
    # Libro más costoso
    libro_mas_costoso = tienda.darLibroMasCostoso()
    if libro_mas_costoso:
        print(f"Libro más costoso: {libro_mas_costoso.toString()}")
    
    # Libro más económico
    libro_mas_economico = tienda.darLibroMasEconomico()
    if libro_mas_economico:
        print(f"Libro más económico: {libro_mas_economico.toString()}")
    
    # Libro más vendido
    libro_mas_vendido = tienda.darLibroMasVendido()
    if libro_mas_vendido:
        print(f"Libro más vendido: {libro_mas_vendido.toString()}")
    
    # Cantidad de transacciones de abastecimiento
    isbn = "9789584276148"
    libro = tienda.buscarLibroPorISBN(isbn)
    if libro:
        transacciones = tienda.darCantidadTransaccionesAbastecimiento(isbn)
        print(f"Transacciones de abastecimiento de '{libro.darTitulo()}': {transacciones}")

if __name__ == "__main__":
    main()
