def edad_usuario(Edad):
    """
    Esta funcion verifica si una persona es mayor de edad o no.
    El programa debe mostrar un mensaje apropiado. Adicionalmente,
    si la edad esta entre 18 y 25 años , debe mostrar un mensaje indicando
    que es un "joven adulto".
    Args:
        edad (int): Edad de la persona.
    Returns:
        str: Mensaje indicando si la persona es mayor de edad, menor de edad,
             o un joven adulto.
    """
    rta = ""

    if Edad < 18:
        rta = (f"Su edad es: {Edad} es menor de edad")
    elif Edad >= 18 and Edad <= 25:
        rta = (f"Su edad es: {Edad} es joven adulto")
    else:
        rta = (f"Su edad es: {Edad} es mayor de edad")

    return rta

Edad = int(input("Ingrese su edad: "))
print(edad_usuario(Edad))
