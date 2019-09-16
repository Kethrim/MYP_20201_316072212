from django.db import models

# Create your models here.
import os

class Buscador():

  def __init__(self,ruta):
    self.ruta = ruta

  def encuentra(self):
    rutas_imagenes = []
    # La funcion os.walk(ruta) 'genera' una terna: (rama, [carpetas], [archivos])
    for rama, carpetas, archivos in os.walk(self.ruta):
      for carpeta in carpetas:
        if carpeta.startswith('.'):
          carpetas.remove(carpeta)
      for archivo in archivos:
        if archivo.endswith('.jpg'):
            rutas_imagenes.append(os.path.join(rama, archivo))
    return rutas_imagenes

a = Buscador('./')