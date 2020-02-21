import numpy as np
from PIL import Image
from archivos import leer_imagen, escribir_imagen


def concatenar_horizontal(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.hstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))

def concatenar_vertical(imagenes):
  min_img_shape = sorted([(np.sum(i.size), i.size) for i in imagenes])[0][1]
  return np.vstack(list((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imagenes)))



if __name__ == '__main__':
    main()
    imagen1 = leer_imagen('1.jpg')
    imagen2 = leer_imagen('2.jpg')

    escribir_imagen('concatenada-vertical.jpg', concatenar_vertical([imagen1, imagen2]))    
    escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal([imagen1, imagen2]))    