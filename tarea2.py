import subprocess

def disco_espacio(particion):
    resultado = subprocess.run(['df', '-h', particion], capture_output=True, text=True)
    lineas = resultado.stdout.split('\n')
    datos = lineas[1].split()

    disco_ocupado = float(datos[4].strip('%'))
    return disco_ocupado

def main ():
    particiones = ['/dev/sda2']
    for particion in particiones:
        porcentaje = disco_espacio(particion)
        print(f"{particion} {porcentaje:.1f}%")

if __name__ == "__main__":
    main()
