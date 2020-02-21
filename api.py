import requests
import json
import os

class PixabayAPI():
  listonga = []

  def __init__(self, key, carpeta_imagenes):
    self.key = key
    self.carpeta_imagenes = carpeta_imagenes
    self.imagenesDescargadas = []

  def buscar_imagenes(self, query, cantidad):
    # URL de búsqueda. Ver la documentación en https://pixabay.com/api/docs/#api_search_images
    url = f'https://pixabay.com/api/?key={self.key}&per_page={cantidad}&q={query}&image_type=photo&lang=es'

    # Hago la request y parseo el JSON que viene como respuesta
    response = requests.get(url)
    jsonResponse = json.loads(response.text)

    # Pero en Python las funciones de listas son funciones globales y no métodos, así que queda así:
    return map(lambda h: h['largeImageURL'], jsonResponse['hits'])  

  def descargar_imagen(self, url):
    # Bajo la imagen (una chorrera de bytes)
    bytes_imagen = requests.get(url)

    # Corto a la URL por cada barra - split('/') - 
    # y me quedo con el último pedazo - [-1] -, 
    # que es el nombre del archivo
    nombre_imagen = url.split('/')[-1]

    # Armo la ruta final del archivo, 
    # el os.path.join mete las barritas en el medio
    ruta_archivo = os.path.join(self.carpeta_imagenes, nombre_imagen)
    with open(ruta_archivo, 'wb') as archivo:
      archivo.write(bytes_imagen.content)
      self.imagenesDescargadas.append(ruta_archivo)
