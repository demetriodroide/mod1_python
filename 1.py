print("=== PROGRAMA: GENERADOR DE PATRÓN TRIANGULAR ===\n")

# Solicitar al usuario la altura del triángulo
# Escribe aquí tu código para pedir el número al usuario
altura = int(input("Introduce la altura del triángulo: "))
ç

# Convertir la entrada a número entero
# Escribe aquí tu código para la conversión
# altura_int = int(altura)

print(f"\nGenerando patrón triangular de altura {altura}:")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
for fila in range(1, altura + 1):
    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    for numero in range(1, fila + 1):

        # Imprimir cada número seguido de un espacio (sin salto de línea)
        print(numero, end=" ")


    # Después de completar una fila, hacer un salto de línea
    print()


print("-" * 30)
print("Patrón completado!")