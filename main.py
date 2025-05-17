from libreria import Libreria
from libro import Libro
from transaccion import Transaccion

def mostrarMenuPrincipal():
    print("\n===== SISTEMA DE GESTIÓN DE LIBRERÍA =====")
    print("1. Registrar un libro en el catálogo")
    print("2. Eliminar un libro del catálogo")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por ISBN")
    print("5. Abastecer ejemplares de un libro")
    print("6. Vender ejemplares de un libro")
    print("7. Calcular cantidad de transacciones de abastecimiento de un libro")
    print("8. Buscar el libro más costoso")
    print("9. Buscar el libro menos costoso")
    print("10. Buscar el libro más vendido")
    print("11. Ver dinero en caja")
    print("12. Ver catálogo completo")
    print("0. Salir")
    print("==========================================")

def mostrarInfoLibro(libro):
    print(f"\nInformación del libro:")
    print(f"ISBN: {libro.darISBN()}")
    print(f"Título: {libro.darTitulo()}")
    print(f"Precio de compra: ${libro.darPrecioCompra()}")
    print(f"Precio de venta: ${libro.darPrecioVenta()}")
    print(f"Cantidad actual: {libro.darCantidadActual()} ejemplares")
    print(f"Total vendidos: {libro.calcularTotalVendidos()} ejemplares")

def main():
    libreria = Libreria()
    
    while True:
        mostrarMenuPrincipal()
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":  # Registrar libro
            isbn = input("Ingrese ISBN: ")
            titulo = input("Ingrese título: ")
            
            try:
                precioCompra = float(input("Ingrese precio de compra: "))
                precioVenta = float(input("Ingrese precio de venta: "))
                
                if precioCompra <= 0 or precioVenta <= 0:
                    print("Los precios deben ser mayores que cero.")
                    continue
                
                if libreria.registrarLibro(isbn, titulo, precioCompra, precioVenta):
                    print(f"Libro '{titulo}' registrado exitosamente.")
                else:
                    print(f"Error: Ya existe un libro con ISBN {isbn}.")
            except ValueError:
                print("Error: Los precios deben ser valores numéricos.")
        
        elif opcion == "2":  # Eliminar libro
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            if libreria.eliminarLibro(isbn):
                print("Libro eliminado exitosamente.")
            else:
                print(f"Error: No se encontró un libro con ISBN {isbn}.")
        
        elif opcion == "3":  # Buscar libro por título
            titulo = input("Ingrese título del libro a buscar: ")
            libro = libreria.buscarLibroPorTitulo(titulo)
            if libro:
                mostrarInfoLibro(libro)
            else:
                print(f"No se encontró un libro con el título '{titulo}'.")
        
        elif opcion == "4":  # Buscar libro por ISBN
            isbn = input("Ingrese ISBN del libro a buscar: ")
            libro = libreria.buscarLibroPorISBN(isbn)
            if libro:
                mostrarInfoLibro(libro)
            else:
                print(f"No se encontró un libro con ISBN {isbn}.")
        
        elif opcion == "5":  # Abastecer ejemplares
            isbn = input("Ingrese ISBN del libro a abastecer: ")
            try:
                cantidad = int(input("Ingrese cantidad de ejemplares a abastecer: "))
                if cantidad <= 0:
                    print("La cantidad debe ser un número positivo.")
                    continue
                
                if libreria.abastecerLibro(isbn, cantidad):
                    print(f"Se abastecieron {cantidad} ejemplares correctamente.")
                    print(f"Dinero en caja: ${libreria.darDineroEnCaja()}")
                else:
                    print("No se pudo realizar el abastecimiento. Verifique el ISBN y que haya suficiente dinero en caja.")
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
        
        elif opcion == "6":  # Vender ejemplares
            isbn = input("Ingrese ISBN del libro a vender: ")
            try:
                cantidad = int(input("Ingrese cantidad de ejemplares a vender: "))
                if cantidad <= 0:
                    print("La cantidad debe ser un número positivo.")
                    continue
                
                if libreria.venderLibro(isbn, cantidad):
                    print(f"Se vendieron {cantidad} ejemplares correctamente.")
                    print(f"Dinero en caja: ${libreria.darDineroEnCaja()}")
                else:
                    print("No se pudo realizar la venta. Verifique el ISBN y que haya suficiente stock.")
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
        
        elif opcion == "7":  # Calcular transacciones de abastecimiento
            isbn = input("Ingrese ISBN del libro: ")
            cantidad = libreria.contarTransaccionesAbastecimientoLibro(isbn)
            if cantidad >= 0:
                print(f"El libro ha tenido {cantidad} transacciones de abastecimiento.")
            else:
                print(f"No se encontró un libro con ISBN {isbn}.")
        
        elif opcion == "8":  # Buscar libro más costoso
            libroMasCostoso = libreria.buscarLibroMasCostoso()
            if libroMasCostoso:
                print("\nEl libro más costoso es:")
                mostrarInfoLibro(libroMasCostoso)
            else:
                print("No hay libros en el catálogo.")
        
        elif opcion == "9":  # Buscar libro menos costoso
            libroMenosCostoso = libreria.buscarLibroMenosCostoso()
            if libroMenosCostoso:
                print("\nEl libro menos costoso es:")
                mostrarInfoLibro(libroMenosCostoso)
            else:
                print("No hay libros en el catálogo.")
        
        elif opcion == "10":  # Buscar libro más vendido
            libroMasVendido = libreria.buscarLibroMasVendido()
            if libroMasVendido:
                ventas = libroMasVendido.calcularTotalVendidos()
                if ventas > 0:
                    print(f"\nEl libro más vendido con {ventas} ejemplares es:")
                    mostrarInfoLibro(libroMasVendido)
                else:
                    print("No hay libros vendidos aún.")
            else:
                print("No hay libros en el catálogo.")
        
        elif opcion == "11":  # Ver dinero en caja
            print(f"Dinero actual en caja: ${libreria.darDineroEnCaja()}")
        
        elif opcion == "12":  # Ver catálogo completo
            catalogo = libreria.darCatalogo()
            if catalogo:
                print("\n===== CATÁLOGO DE LIBROS =====")
                for libro in catalogo:
                    print(f"ISBN: {libro.darISBN()} - Título: {libro.darTitulo()} - " +
                          f"Precio: ${libro.darPrecioVenta()} - Stock: {libro.darCantidadActual()}")
            else:
                print("El catálogo está vacío.")
        
        elif opcion == "0":  # Salir
            print("Gracias por usar el sistema de gestión de librería.")
            break
        
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()