import os

nombre = input("Nombre del archivo: ").strip().lower()
encontrado = False

for carpeta, _, archivos in os.walk(os.path.expanduser("~")):
    for archivo in archivos:
        if os.path.splitext(archivo)[0].lower() == nombre:
            print(os.path.join(carpeta, archivo))
            encontrado = True

if not encontrado:
    print("Archivo no encontrado.")
