#include <stdio.h>

int esPrimo(int num){
    int i =2;
    for (i; i<num; i++){
        if (num%i == 0) return 0;
    }
    return 1;
}

int main(){
    printf("Dame un número ");
    int n;
    int *a= &n;
    scanf("%i",a);
    for(int j=2; j<n; j++){
        if (esPrimo(j)) printf("%i \n",j);
    }

    return 0;
}
