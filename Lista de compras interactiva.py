def lista_compras_interactiva():
    """
    Esta funcion permite al usuario crear una lista de compras interactiva.
    El usuario puede agregar, eliminar y ver los elementos de la lista o
    salir de la aplicación.
    """
    lista = []

    while True:
        print("\nBienvenido ¿Que desea hacer?:")
        print("1. Agregar un producto a la lista")
        print("2. Eliminar un producto de la lista")
        print("3. Ver la lista de compras")
        print("4. Salir de la aplicación")

        accion = input("Digite el numero de la accion que desea realizar ")

        if accion == "1":
            produ = input("Ingrese el nombre del producto ")
            lista.append(produ)
            print(f"{produ} ha sido agregado a la lista.")

        elif accion == "2":
            produ = input("Ingrese el nombre del producto a eliminar: ")
            if produ in lista:
                lista.remove(produ)
                print(f"{produ} ha sido eliminado de la lista.")
            else:
                print(f"{produ} no se encuentra en la lista.")

        elif accion == "3":
            if lista:
                print("Lista de compras:")
                for i, produ in enumerate(lista, start=1):
                    print(f"{i}. {produ}")
            else:
                print("La lista de compras está vacía.")

        elif accion == "4":
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break

        else:
            print("Acción no reconocida. Por favor, intente nuevamente.")

lista_compras_interactiva()