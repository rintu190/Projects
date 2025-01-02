#include<stdio.h>
int isPrime(int n){
    for(int i =2;i<=n/2;i++){
        if(!(n%i))
            return 0;
    }
    return 1;
}
void main(){
    int numPrimes =0;

    for(int i =2;i<250001;i++){
        numPrimes+=isPrime(i);
    }
    printf("%d\n",numPrimes);
}