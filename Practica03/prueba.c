#include "quickSortParalelo.c"
#include <time.h>
#include <stdio.h>
#define SIZE 10000000
/**
* Llena arreglo con números aleatorios.
*/
void llenaArreglo(int *arreglo, int size)
{
  srand(time(NULL));
  for (int i = 0; i < size; i++) {
    int r = rand();
    arreglo[i] = r;
  }
}

/**
* Devuelve 1 si está ordenado 0 si no.
*/
int isSorted(int *arreglo, int size){
  int last = arreglo[0];
  for (int i = 0; i < size; i++) {
    if(last > arreglo[i]) {
      return 0;
  }
  }
  return 1;
}

int main() {
  int *arreglo = malloc(SIZE * sizeof(int));
  llenaArreglo(arreglo,SIZE);

  int *arreglo2 = malloc(SIZE * sizeof(int));
  llenaArreglo(arreglo2, SIZE);

  clock_t t;
  t = clock();
  QuickSort(arreglo, 0, SIZE-1);
  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC;

  if(isSorted(arreglo,SIZE))
  printf("\nQuickSort secuencial con %i elementos toma %f segundos en ejecutarse\n",SIZE, time_taken);
  else printf("\nQuickSort secuencial no funciona.\n");

  t = clock();
  int numHilos = 2;
  int indices[numHilos][2];
  quickSortParalelo(arreglo2,SIZE);
  t = clock()-t;
  time_taken = ((double)t)/CLOCKS_PER_SEC;

  if(isSorted(arreglo2,SIZE))
  printf("\nQuickSort paralelo con %i elementos toma %f segundos en ejecutarse\n",SIZE, time_taken);
  else printf("\nQuickSort paralelo no funciona.\n");

  free(arreglo);
  free(arreglo2);
  return 0;
}
