# Para leer archivos desde python se usa with open(parameters) as f:
# r = read / leer
# w = escritura
# x = crear
# with open(archivo.txt, "r"):

try:
    with open("archivo.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("Archivo no encontrado ")
