#include <stdio.h>
#include <math.h>
#include <omp.h>
#include "QuickSort.c"

/**
*Método que sobreescribe los elementos de un arreglo ordenado en uno desordenado.
*@param arregloOrdenado- arreglo que ya está ordenado.
*@param arregloDesordenado- arreglo que se sobreescribirá.
*@param tam- tamanio del arreglo ordenado.
*/
void sobreEscribeArreglo(int arregloOrdenado[], int arregloDesordenado[], int tam){
  for (int k = 0; k < tam; k++) {
    arregloDesordenado[k] = arregloOrdenado [k];
  }
}

/**
*Método que mezcla dos intervalos ordenados desde el índice 0.
*int a- arreglo ordenado en dos intervalos.
*int inicio2- índice donde inicia el segundo intervalo ordenado.
*int fin2- donde termina el segundo intervalo ordenado.
*/
void merge(int a[], int inicio2, int fin2) {
  int i = 0;
  int j = inicio2;
  int *arregloOrdenado = malloc((fin2+1)* sizeof(int));
  int indiceArregloOrdenado = 0;
  while (j<=(fin2) && i<(inicio2)){
    if (a[i]>=a[j]){
      arregloOrdenado[indiceArregloOrdenado] = a[j];
      j+=1;
    } else {
      arregloOrdenado[indiceArregloOrdenado] = a[i];
      i+=1;
    }
    indiceArregloOrdenado +=1;
  }
  if(j>(fin2))
  while (i<inicio2) { 
    arregloOrdenado[indiceArregloOrdenado] = a[i];
    i+=1;
    indiceArregloOrdenado+=1;
  }
    sobreEscribeArreglo(arregloOrdenado, a, j);
    free(arregloOrdenado);
  }

/**
*Método que reliza el ordenamiento quickSort en paralelo.
*@param arregloDesordenado- arreglo sobre el cuál se hará quickSort.
*@param indices- arreglo de dos dimensiones en la que se listan los intervalos en tuplas, donde inicia y donde termina cada uno.
*@param numHilos- cantidad de hilos que se usarán.
*/
void quickSortParalelo(int arregloDesordenado[], int tam){
  int div = tam/2;
  omp_set_num_threads(2);
  #pragma omp parallel sections
  {
      #pragma omp section
      QuickSort(arregloDesordenado, 0, div-1);
      #pragma omp section
      QuickSort(arregloDesordenado, div, tam-1);
  }
    merge(arregloDesordenado, div, tam-1);
}
