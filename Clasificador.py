import sys
import os
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
      self.pingu = class_pingu()
    except Exception as e:
      print("No se pueden cargar los modelos.")

  def queAnimalEs(self,ruta):
    try:
      if self.hipo.is_hippo(ruta):
        return 'Es un hipopotamo!'
      elif self.cuyo.es_cuyo(ruta):
        return 'Es un cuyo!'
      elif self.jirf.esJirafa(ruta):
        return 'Es una jirafa!'
      elif self.ave.evaluar(ruta):
        return 'Es un avestruz!'
      if self.pingu.esPinguino(ruta):  
        return 'Es un pinguino!'
      else:
        return 'No es ningún animal.'      
    except Exception as e:
      return 'Ingresa una nueva ruta.'
         
    
#ruta = sys.argv[1]
# c = clasificador()
# for imagen in os.listdir("revision"):
#   ruta = os.path.join("revision",imagen)  
#   print("\t",ruta, c.queAnimalEs(ruta)) 
