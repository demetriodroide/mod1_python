# Solicitar la edad al usuario
edad = int(input("Que edad tienes ?"))
# Convertir la entrada a entero

int(edad)
# Evaluar la edad usando if-elif-else

if edad > 18:
    print("Eres mayor de edad")
elif edad < 18:
    print ("Eres menor de edad")
else:
    print("tienes 18 años exactos")

# Mostrar el mensaje correspondiente
print(f"Tienes exactamente {edad} años")