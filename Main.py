import sys
from Clasificador import clasificador
ruta = sys.argv[1]
c = clasificador() 
print("\t", c.queAnimalEs(ruta))