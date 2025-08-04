def tabla_multi(num):
    """
    Imprime la tabla de multiplicar del número dado hasta el límite especificado.

    Args:
        num (int): El número del cual se desea imprimir la multiplicacion.


    """
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")

num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multi(num)