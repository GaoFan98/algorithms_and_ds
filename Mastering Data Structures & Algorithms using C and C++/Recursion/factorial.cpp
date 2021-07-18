#include <iostream>
using namespace std;

// first method recursion T=O(n), S=O(n)
// int facorial_recursion(int n){
//     if (n<=1)
//     {
//         return 1;
//     }
    
//     return facorial_recursion(n-1)*n;
// }

// int main(){
//     int n = 5;
//     cout<<facorial_recursion(n);
// }

// second method loop O(n)
int facorial_recursion(int n){
    int f=1;
    int i;

    for (i = 1; i <= n; i++)
    {
        f=f*i;
    }

    return f;
}

int main(){
    int n = 5;
    cout<<facorial_recursion(n);
}