def agenda_de_contactos():
    """
    Esta función permite al usuario crear una agenda de contactos utilizando un diccionario.
    El usuario puede agregar, buscar y ver los contactos a traves de funciones.

    Arg:
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono del contacto.
    Returns:
        None
    """
    agenda = {}

    def agregar_contacto(nombre, telefono):
        agenda[nombre] = telefono
        print(f"Contacto {nombre} ha sido agregado.")

    def buscar_contacto(nombre,telefono):
        if nombre in agenda:
            print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def ver_contactos():
        if agenda:
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda está vacía.")

    while True:
        print("\nBienvenido a la agenda de contactos. ¿Qué desea hacer?")
        print("1. Agregar un contacto")
        print("2. Buscar un contacto")
        print("3. Ver todos los contactos")
        print("4. Salir")

        accion = input("Digite el número de la acción que desea realizar: ")

        if accion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono del contacto: ")
            agregar_contacto(nombre, telefono)

        elif accion == "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre,telefono)

        elif accion == "3":
            ver_contactos()

        elif accion == "4":
            print("Saliendo de la agenda de contactos. ¡Hasta luego!")
            break

        else:
            print("Acción no reconocida. Por favor, intente nuevamente.")

agenda = agenda_de_contactos()
