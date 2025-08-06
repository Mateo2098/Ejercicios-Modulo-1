def agregar_producto(inventario):
    """
    Agregar productos al inventario.

    Args:
        inventario (list): Lista de productos

    """
    nom = input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio del producto: "))
    cant = int(input("Ingrese la cantidad disponible: "))

    produ = {
        "nombre": nom,
        "precio": precio,
        "cantidad": cant
    }
    inventario.append(produ)
    print(f"El producto '{nom}' fue agregado correctamente.\n")


def realizar_venta(inventario):
    """
    Realizar la venta de un producto y actualiza la venta.

    Args:
        inventario (list): Lista de productos
    """
    nom = input("Ingrese el nombre del producto de la venta: ").strip()
    cant_vendida = int(input("Cantidad vendida: "))

    for producto in inventario:
        if producto["nombre"].lower() == nom.lower():
            if producto["cantidad"] >= cant_vendida:
                producto["cantidad"] -= cant_vendida
                total = producto["precio"] * cant_vendida
                print(f"La venta realizada. Total: ${total:.2f}\n")
                return
            else:
                print("No hay suficiente stock para realizar la venta.\n")
                return
    print("Producto no encontrado.\n")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos que hay en el inventario.

    Args:
        inventario (list): Lista de productos
    """
    if not inventario:
        print("Inventario vacío.\n")
        return

    print("Inventario de productos:")
    for producto in inventario:
        print(f"• {producto['nombre']} - ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
    print()


def sistema_inventario():
    """
    Esta funcion gestiona un sistema interactivo para el inventario de una tienda
    Permitiendo agregar productos, realizar ventas y mostrar el inventario.

    """
    inventario = []

    while True:
        print("\nMENÚ DEL INVENTARIO")
        print("1. Agregar productos")
        print("2. Realizar ventas")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción 1-4: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            realizar_venta(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("hasta luego")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

sistema_inventario()