def consultar_saldo(saldo):
    """
    Muestra el saldo actual del usuario.

    Args:
        saldo (float): Saldo disponible en la cuenta.
    """
    print(f"Saldo actual: ${saldo:.2f}")


def depositar(saldo):
    """
    Solicita al usuario una cantidad a depositar y actualiza el saldo.

    Args:
        saldo (float): Saldo antes del depósito.

    Returns:
        float: Saldo actualizado tras el depósito.
    """
    monto = float(input("Ingresa el monto a depositar: $"))
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    else:
        print("El monto debe ser positivo.")
    return saldo


def retirar(saldo):
    """
    Solicita al usuario una cantidad a retirar y actualiza el saldo si hay fondos suficientes.

    Args:
        saldo (float): Saldo antes del retiro.

    Returns:
        float: Saldo actualizado tras el retiro (si fue exitoso).
    """
    monto = float(input("Ingresa el monto a retirar: $"))
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
    elif monto > saldo:
        print("Fondos insuficientes para realizar el retiro.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    return saldo


def cajero_automatico():
    """
    Simula las operaciones de un cajero automático.

    Permite al usuario consultar saldo, depositar, retirar y salir del programa.
    """
    saldo = 1000000.00
    print("Bienvenido al cajero automático. Saldo inicial: $1000000.00")

    while True:
        print("\nMENÚ")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "4":
            print("¡Hasta luego! No olvide retirar su tarjeta.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

cajero_automatico()