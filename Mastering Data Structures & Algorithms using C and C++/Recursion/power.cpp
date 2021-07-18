#include <iostream>
using namespace std;

// first method recursion T=O(n), S=O(n)
// int power_rec(int m,int n){
//     if (n==0){
//         return 1;
//     }

//     return power_rec(m,n-1)*m;
// }

// int main(){
//     int m;
//     int n;

//     cout<<power_rec(m=5,n=3);
// }

// second method
int power_rec(int m,int n){
    if (n==0){
        return 1;
    }
    if(n%2==0){
        return power_rec(m*m,n/2);
    }
    else {
        return m*power_rec(m*m,n/2);
    }
}

int main(){
    int m;
    int n;

    cout<<power_rec(m=2,n=9);
}