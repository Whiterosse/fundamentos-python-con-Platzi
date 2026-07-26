"""🛠️ Reto 1: El Validador de ID de Clientes (Nivel: Inicial)
***Problema:** Estás creando un sistema donde el usuario debe ingresar su ID de cliente para consultar su suscripción. Si el usuario
ingresa letras en lugar de números, el sistema no debe romperse.

***Tu Misión:** Escribe un programa con un bucle `while` infinito que pida el ID (solo números). Usa `try/except` con `ValueError`
para atrapar el error si ingresa texto. Si ingresa el número correctamente, rompe el bucle con `break` y muestra un mensaje de éxito.
"""

while True:
    try:
        identificacion = int(input("Ingresa tu ID. (acepta solo numeros positivos): "))
        if identificacion > 0:
            print("Login accept")
            break
        else:
            print("El ID no debe ser 0")
    except ValueError:
        print("Solo se permiten numeros ")
