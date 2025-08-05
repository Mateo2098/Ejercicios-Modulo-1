# Diccionario de factores de conversión relativos a 1 metro
conversiones = {
    'metro': 1.0,
    'centimetro': 0.01,
    'milimetro': 0.001,
    'kilometro': 1000.0,
    'pulgada': 0.0254
}

def convertir_unidades(valor, unidad_origen, unidad_destino):
    """
    Convierte una cantidad , recibe una unidad de origen y la unidad de destino
    y realiza la conversión.
    Args:
        valor (float): Cantidad a convertir.
        unidad_origen (str): Unidad de medida de origen.
        unidad_destino (str): Unidad de medida de destino.
    Returns:
        float: Valor convertido a la unidad de destino.
    """

    unidad_origen =  unidad_origen.lower()
    unidad_destino = unidad_destino.lower()

    if unidad_origen not in conversiones:
        print(f"Unidad de origen '{unidad_origen}' no reconocida.")
        return None
    if unidad_destino not in conversiones:
        print(f"Unidad de destino '{unidad_destino}' no reconocida.")
        return None

    valor_metros = valor * conversiones[unidad_origen]
    valor_convertido = valor_metros / conversiones[unidad_destino]
    return valor_convertido

if __name__ == "__main__":
    try:
        valor = float(input("Ingrese el valor a convertir: "))
        unidad_origen = input("Ingrese la unidad de origen (metro, centimetro, milimetro, kilometro, pulgada): ")
        unidad_destino = input("Ingrese la unidad de destino (metro, centimetro, milimetro, kilometro, pulgada): ")

        resultado = convertir_unidades(valor, unidad_origen, unidad_destino)
        if resultado is not None:
            print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}.")
    except ValueError:
        print("Por favor, ingrese un número válido para el valor.")
