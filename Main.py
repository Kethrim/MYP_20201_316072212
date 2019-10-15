import sys
from clasificador.hippo_classifier import HippoClassifier as clas_hipo
from clasificador.clasificadorCuyo import ClasificadorCuyo as clas_cuyo
from clasificador.clasificadorJirafa import clasificadorJirafa as clas_jirf
from clasificador.Clasificador_Avestruz import Clasificador_Avestruz as clas_aves

hipo = clas_hipo('modelos/hippo_model.h5')
cuyo = clas_cuyo()
jirf = clas_jirf()
avestruz = clas_aves()

ruta = sys.argv[1]

if hipo.is_hippo(ruta):
  # falla con revision/cuyo_prueba.jpg, dice que es un hipo
  print('Es un hipopotamo!')
elif False:  
  print('Pinguino')
elif avestruz.evaluar(ruta):
  print('Avestruz')
elif cuyo.es_cuyo(ruta):
  print('Es un cuyo!')
elif jirf.esJirafa(ruta):
  print('Es una jirafa!')  
else:
  print('No es nada')