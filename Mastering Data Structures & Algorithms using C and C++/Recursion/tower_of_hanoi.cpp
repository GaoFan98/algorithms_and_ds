#include <iostream>
using namespace std;

// O(2**n)
void hanoi(int n, int A, int B, int C){
    if (n>0){
        hanoi(n-1,A,C,B);
        printf("disk number %d from %d to %d\n",n,A,C);
        hanoi(n-1,B,A,C);
    }
}

int main(){
    int n;
    int A;
    int B;
    int C;

    hanoi(n=3,A=1,B=2,C=3);
}