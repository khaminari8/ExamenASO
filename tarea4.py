import logging
import shutil

def analizar ():

    logging.basicConfig(filename="/home/khami/logs/espacio.log", level=logging.INFO, 
                    format="%(asctime)s- %(levelname)s: %(message)s")

    total, used, free = shutil.disk_usage("/")

    porcentaje = (used / total) * 100

    if porcentaje > 80:
        logging.error(f"Espacio en Raiz {porcentaje:.2f}%")
    elif porcentaje > 60:
        logging.warning(f"Espacio en Raiz {porcentaje:.2f}%")
    else:
        logging.info(f"Espacio en Raiz {porcentaje:.2f}%")

if __name__ == "__name__":
    analizar()