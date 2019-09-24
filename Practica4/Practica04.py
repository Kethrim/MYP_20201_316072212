#Practica 4
#Equipo Salsabrozos ;V
#Integrantes :
 #Ketrhim
 #Brayan
 #Jose
 #Erick
 #Yo merengues


#Libreria para nevegar entre las carpetas
import os
#Maneja imagenes
import cv2
#Maneja matrices gigantescas
import numpy as np
#Generar acciones aleatorias
import random
# convierte objetos de Python en una secuencia de bytes
import pickle


 #Clase que obtiene imagenes entre un directorio y las separa 
class Preprocess:
    def _init_(self):
        #tamaño por defecto de la imagen
        self.IMG_SIZE = 50
        #Arreglo que almacenara todas las imagenes de cada carpeta
        self.trainig_data = []
        #almacena las imagenes
        self.fetures = []
        #almacena las etiquetas
        self.labels = []
        #Añmacena los subdirectorios
        self.subdirectories = []

    #Obtenemos los subdirectorios de una carpeta
    def get_subdirectories(self, Directory):
        #iteramos sobre cada elemento de la carpeta
        for sub in os.listdir(Directory):
            path = os.path.join(Directory,sub)
            #si es un directorio lo anexamos ala lista para procesarlo despues
            if os.path.isdir(pathname):
                self.subdirectories.append(path)
                #Hacemos recursion sobre el subdirectorio obtenido 
                self.get_subdirectories(path)          
          
        return

     #Obtiene las imagenes de cada uno de los subdirectorios
     def load_training_data(self):
		for category in self.subdirectories:
            path = category
			class_num = self.CATEGORIES.index(category)
			for img in os.listdir(path):
                try:
                    ##Se modifica la imagen a una escala de grises
					img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                    #Se modifica el tamaño de la imagen
					new_array = cv2.resize(img_array,(self.IMG_SIZE,self.IMG_SIZE))
                     #Agregamos la imagen junto con su etiqueta al trainig Data 
					self.training_data.append([new_array,class_num])
				except Exception as e:
					pass   


     #Separamos las imagenes por etiqueta
	def split_and_prepare(self):
		random.shuffle(self.training_data)
		for features, label in self.training_data:
			self.features.append(features)
			self.labels.append(label)
		self.features = np.array(self.features).reshape(-1,self.IMG_SIZE,self.IMG_SIZE,1)
		self.features = self.features/255.0


    #Almacenamos cada objeto de los arreglos features y labels en un archivo de bytes
	def write_out(self):
		pickle_out = open("X.pickle","wb")
		pickle.dump(self.features,pickle_out)
		pickle_out.close()
         
		pickle_out = open("Y.pickle","wb")
		pickle.dump(self.labels,pickle_out)
		pickle_out.close()


#instanciamos un objeto de tipo processor
processor = Preprocess()
#obtenemos todas las subcarpetas
processor.get_subdirectories("Data");
#Procesamos cada imagen de cada subcarpeta 
processor.load_img_list()
# Se separan las listas de las imágenes leídas.
processor.split_and_prepare()
#Se guardan las imagenes en un archivo binario
processor.write_out()


            

			

   