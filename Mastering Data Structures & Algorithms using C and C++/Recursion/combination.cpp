// combination formula of selecting the possible ways
// for instance, ABCDEF given, the number of select 3 letters =>
// ABC,ACB,BAC, etc...

// nCr = n! / r!(n-r)!
// where n is number of total integers and r is permutation number

#include <iostream>
using namespace std;

// recursion method with factorial function O(n)
// int factorial(int n){
//     if (n<=1) return 1;
    
//     return factorial(n-1)*n;
// }

// int permutation(int n,int r){
//     int t1,t2;
//     t1=factorial(n);
//     t2=factorial(r)*factorial(n-r);

//     return t1/t2;
// }

// int main(){
//     int n;
//     int r;

//     cout<<permutation(n=4,r=2);
// }

// recursive -> Pascal's triangle
double pascal_trinagle(int n,int r){
    if (r==0 || n==r) return 1;

    else return pascal_trinagle(n-1,r-1)+pascal_trinagle(n-1,r);
}

int main(){
    int n;
    int r;

    cout<<pascal_trinagle(n=4,r=2);
}