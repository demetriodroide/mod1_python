""""
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

print(f" 12Tienes exactamente {edad} años")
"""

# LOGIN CON NÚMERO MÁXIMO DE INTENTOS

# Aquí podemos crear una aplicación de consola
# que pida al usuario email y password,
# si falla tres veces detiene el programa y no deja continuar
# si acierta le deja usar la aplicación

VALID_EMAIL = ""
VALID_PASSWORD = ""

def login():
# bucle for para máximo 3 intentos fallidos
# leer por input
for i in input(VALID_EMAIL) 
return True

def elegir_opcion():
print("")
opcion = input()
return opcion


if login():
opcion = elegir_opcion()
# hacer algo en base a la opcion elegida por el usuario:
# if...
# elif...
# elif...
# else+