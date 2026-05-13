# Función recursiva para calcular el factorial de un número
def factorial(n):

    # CASO BASE:
    # Si n es igual a 0, el factorial es 1.
    # Aquí se detiene la recursión para evitar llamadas infinitas.
    if n == 0:
        return 1

    # PASO RECURSIVO:
    # La función se llama a sí misma con (n-1)
    # y multiplica el resultado por n
    else:
        return n * factorial(n - 1)


# Ejemplo de uso del algoritmo
numero = 5
resultado = factorial(numero)

# Mostrar el resultado
print("El factorial de", numero, "es:", resultado)
