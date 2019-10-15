import sys
from clasificador.hippo_classifier import HippoClassifier as clas_hipo
from clasificador.clasificadorCuyo import ClasificadorCuyo as clas_cuyo
from clasificador.clasificadorJirafa import clasificadorJirafa as clas_jirf
from clasificador.Clasificador_Avestruz import Clasificador_Avestruz as clas_ave
from clasificador.clasificadorPinguino import clasificadorPinguino as class_pingu
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
      self.ave = clas_ave()  
      self.pingu = class_pingu
    except Exception as e:
      print("No se pueden cargar los modelos.")


  def queAnimalEs(self,ruta):
    if self.pingu.esPinguino(ruta):  
      return 'Es un pinguino!'
    elif self.jirf.esJirafa(ruta):
      return 'Es una jirafa!'
    elif self.hipo.is_hippo(ruta):
      return 'Es un hipopotamo!'
    elif self.ave.evaluar(ruta):
      return 'Es un avestruz!'
    elif False: #revision/albaca.jpg
      return 'Es un cuyo!'
    else:
      return 'No es ninigún animal.'


ruta = sys.argv[1]
c = clasificador()
print("\t", c.queAnimalEs(ruta))
