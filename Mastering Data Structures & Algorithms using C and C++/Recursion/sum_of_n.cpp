#include <iostream>
using namespace std;

// first method recursion T=O(n), S=O(n)
// int sum_of_n(int n){
//     if (n == 0) {
//         return 0;
//     }
//     return sum_of_n(n-1)+n;
// }

// int main(){
//     int n = 6;
//     cout<<sum_of_n(n);
// }

// second method O(1)
// int sum_of_n(int n){
//     return n*(n+1)/2;
// }

// int main(){
//     int n = 6;
//     cout<<sum_of_n(n);
// }

// third method loop O(n)
int sum_of_n(int n){
    int i,s=0;

    for (i = 1; i <= n; i++)
    {
        s+=i;
    }

    return s;
}

int main(){
    int n = 6;
    cout<<sum_of_n(n);
}