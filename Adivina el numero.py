def adivina_el_numero():
    """
    Esta funcion implementa un juego en el que el usuario debe adivinar un número secreto
    predeterminado por el programa.
    Args:
        None
    :return:
        cant de intentos que le tomó al usuario adivinar el número.
    """
    numero_secreto = 42
    cant = 0
    num = 0

    while num != numero_secreto:
        num = int(input("Ingresa el número secreto" ))
        cant += 1
        if num < numero_secreto:
            print("El número ingresado es menor que el numero secreto.")
        elif num > numero_secreto:
            print("El número ingresado es mayor que el numero secreto.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {cant} intentos.")
    return cant

adivina_el_numero()





