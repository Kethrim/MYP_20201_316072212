#%%
import os
#Maneja imagenes
import cv2
#Maneja matrices gigantescasls
import numpy as np
#Generar acciones aleatorias
import random
# convierte objetos de Python en una secuencia de bytes
import pickle
import matplotlib.pyplot as plt 


 #Clase que obtiene imagenes entre un directorio y las separa
class Preprocess:
    def __init__(self):
        #tamaño por defecto de la imagen
        self.IMG_SIZE = 50
        #Almacena
        self.Data=["Hipopotamo","no Hipo"]
        #Arreglo que almacenara todas las imagenes de cada carpeta
        self.training_data = []
        #almacena las imagenes
        self.features = []
        #Almacena los subdirectorios
        self.subdirectories = []
        #almacena las etiquetas
        self.labels = []
        #Añmacena los subdirectorios

    #Obtenemos los subdirectorios de una carpeta
    def get_subdirectories(self, Directory):
        """ recibe la direccion de un directorio y obtiene todas las subcarpetas contenidas
            en ella.
    
            @type  Directory: string 
            @param Directory: ruta del directorio
            
        """
         #iteramos sobre cada elemento de la carpeta
        for sub in os.listdir(Directory):
            path = os.path.join(Directory,sub)
            #si es un directorio lo anexamos ala lista para procesarlo despues
            if os.path.isdir(path):
                self.subdirectories.append(path)
                #Hacemos recursion sobre el subdirectorio obtenido
                self.get_subdirectories(path)

        return

     #Obtiene las imagenes de cada uno de los subdirectorios
    def load_training_data(self):
        """ 
            lee todas las imagenes contenidas en los subdirectorios y las modifica, 
            les asigna una etiqueta indicando lo que son ,0 -Hipopotamo, 1-otra cosa 
        """
        for category in self.subdirectories:
            path = category
            class_num = self.subdirectories.index(category)
            for img in os.listdir(path):
                try:
                    ##Se modifica la imagen a una escala de grises
                    img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                    #Se modifica el tamaño de la imagen
                    new_array = cv2.resize(img_array,(self.IMG_SIZE,self.IMG_SIZE))
                    self.training_data.append([new_array,class_num])
                except Exception as e:
	                pass


     #Separamos las imagenes por etiqueta
    def split_and_prepare(self):
        """ revuelve todas las imagenes leidas y las separa por imagenes y por etiquetas
        """
        random.shuffle(self.training_data)
        for features,label in self.training_data:
            self.features.append(features)
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.IMG_SIZE, self.IMG_SIZE,1)
        self.features = self.features/255.0


    #Almacenamos cada objeto de los arreglos features y labels en un archivo de bytes
    def write_out(self):
        pickle_out = open("X.pickle","wb")
        pickle.dump(self.features,pickle_out)
        pickle_out.close()
        pickle_out = open("Y.pickle","wb")
        pickle.dump(self.labels,pickle_out)
        pickle_out.close()

        
        
        
        
p=Preprocess()
p.get_subdirectories("./Practica4/Data")
p.load_training_data()
p.split_and_prepare()
p.write_out()



#%%
