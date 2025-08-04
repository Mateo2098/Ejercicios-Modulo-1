def Conta_vocales_consonantes(texto):
    """
    Cuenta el número de vocales y consonantes en un texto dado.

    Args:
          texto (str): Texto ingresado por el usuario.

    Returns:
         conteo: numeró de vocales y consonantes del texto.
    """
    vocales = ['a', 'e', 'i', 'o', 'u']
    conteoV = 0
    conteoC = 0

    texto_Nuevo = texto.replace(" ","").lower()

    for i in texto_Nuevo:
        if ord(i) >= 97 and ord(i) <= 122:
            if i in vocales:
                conteoV += 1
            else:
                conteoC += 1
        else:
            print(f"{i} no es una letra del alfabeto")

    return {"vocales" : conteoV, "consonantes": conteoC}

texto = input("Ingrese un texto: ")
result = Conta_vocales_consonantes(texto)

print(f"El total de vocales es: {result['vocales']}")
print(f"El total de consonantes es: {result['consonantes']}")



