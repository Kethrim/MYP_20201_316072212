import sys
from clasificador.hippo_classifier import HippoClassifier as clas_hipo
from clasificador.clasificadorCuyo import ClasificadorCuyo as clas_cuyo
from clasificador.clasificadorJirafa import clasificadorJirafa as clas_jirf

class clasificador():
  """
  Clase que clasifica una imagen en:
  hipopótamo
  pinguino
  avestruz
  jirafa
  cuyo
  otro.
  """
  
  def __init__(self):
  """
  Se cargan los modelos previamente creados de cada animal.
  """
  try:
    self.hipo = clas_hipo('modelos/hippo_model.h5')
    self.cuyo = clas_cuyo()
    self.jirf = clas_jirf()    
  except Exception as e:
    print("No se pueden cargar los modelos.")


  def queAnimalEs(self,ruta):
    if self.hipo.is_hippo(ruta):
      return 'Es un hipopotamo!'
    elif False:  
      return 'Es un pinguino!'
    elif False:
      return 'Es un avestruz!'
    elif self.cuyo.es_cuyo(ruta):
      return 'Es un cuyo!'
    elif self.jirf.esJirafa(ruta):
      return 'Es una jirafa!'
    else:
      return 'No es nada'


ruta = sys.argv[1]
c = clasificador()
print(c.queAnimalEs(ruta))
