import logging
from api import PixabayAPI
import threading
from concatenacion import *
from archivos import leer_imagen, escribir_imagen


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


carpeta_imagenes = './imagenes'
query = input('Que imagenes desea buscar??\n')
cant = int(input(f'Cuantas imagenes de {query} quiere descargar??\n'))
api = PixabayAPI('15310263-3c077b8973067ba768708060a', carpeta_imagenes)
urls = api.buscar_imagenes(query, cant)
logging.info(f'Buscando imagenes de {query}...')

for u in urls:
    t = threading.Thread(target = api.descargar_imagen, args=[u])
    logging.info(f'Descargando {u}')
    for imagen in api.imagenesDescargadas:
        leer_imagen(api.imagenesDescargadas)
        escribir_imagen('concatenada-vertical.jpg', concatenar_horizontal([u, u+1]))
    t.start()
    t.join()
print(api.imagenesDescargadas)



