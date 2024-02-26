import os

for i in range (1, 6):
    carpeta = f"folder{1}"
    os.makedirs(carpeta, exist_ok=True)

for j in range (1, 11):
    archivo = f"{carpeta}/fichero{j}.txt"
    with open(archivo, 'w') as file:
        file.write(f"Contenido del fichero {j}")