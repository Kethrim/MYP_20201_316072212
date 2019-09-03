#include <stdio.h>
#include <stdlib.h>
/*
Función que intercambia dos elementos un en arreglo, los parámetr i,j deben de ser menores al tamaño del arreglo-1 y mayores que 0.
param- a, arreglo en el que se trabaja.
param- i, lugar que se intercambia con j.
param- j, lugar que se intercambia con i.
*/
void swap(int a[], int i, int j) {
  int aux = a[i];
  a[i]= a[j];
  a[j]= aux;
}

/*
Función que particiona un arreglo de manera que de lado derecho quedan todos los mayores al pivote y de lado izquierdo los menores a él.
El pivote se obtiene a la mitad del arreglo.
param- array, arreglo sobre el que se traajará.
param- inicio, a partir de dónde se particionará el arreglo.
param. fin, hasta dónde se particionará el arreglo.
return el ínidice dónde se encuentra el pivote ordenado.
*/
int particion(int array[], int inicio, int fin){
  if (inicio>= fin) return 0;
  int indexPivote = (fin+inicio)/2;
  int pivote = array[indexPivote];
  int i = inicio;
  int j = inicio-1;
  swap(array, indexPivote, fin);
  for (i; i < fin; i++) {
    if (array[i]< pivote){
      j= j+1;
      swap(array,i,j);
    }
  }
  swap(array,i,j+1);
  return j+1;
}

/*
Método que realiza QuickSort a un arreglo.
param- array, arreglo donde se trabajará.
param- inicio, índice donde inicia el arreglo.
param fin, índice donde termina el arreglo.
*/
void QuickSort(int array[], int inicio, int fin) {
  if (inicio<fin){
    int pivote = particion(array, inicio, fin);
    QuickSort(array, inicio, pivote-1);
    QuickSort(array, pivote+1, fin);
  }
}
