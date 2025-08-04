def validador_palindromo(palabra):
    """
    Validar si una palabra es un palíndromo.

    Args:
         palabra (str): La palabra a validar.
    Returns:
        str: Mensaje indicando si la palabra es un palíndromo o no.
    """
    frase = palabra.replace(" ", "").lower()
    rta = ""

    if frase == frase[::-1]:
        rta = f"La palabra '{palabra}' es un palíndromo."
    else:
        rta = f"La palabra '{palabra}' no es un palíndromo."
    return rta

palabra = input("Ingrese una palabra o frase para validar si es un palíndromo: ")
resultado = validador_palindromo(palabra)
print(f"{palabra} : {resultado}")
