#include <iostream>
using namespace std;

// recursion O(2**n)
// int fibo(int n){
//    if (n<=1) return n;

//     return fibo(n-2)+fibo(n-1);
// }

// int main(){
//     int n;
//     cout<<fibo(7);
// }

// iterative approach O(n)
// int fibo_it(int n){
//     int current = 0;
//     int next = 1;
//     int sum;
//     int i;

//     if (n<=1) return n;

//     for(i=2; i<=n;i++){
//         sum=current+next;
//         current=next;
//         next=sum;
//     }

//     return sum;
// }

// int main(){
//     int n;
//     cout<<fibo_it(7);
// }

// memoization (table) approach O(n)
// int fibo_m(int n){
//     int F[n];   
//     int i;

//     for (i=0; i<n; i++){
//         F[i] = -1;
//     }
//     if (n<=1) {
//         F[n]=n; 

//         return n;
//     }else{
//         if (F[n-2]==-1)
//             F[n-2] = fibo_m(n-2);
         
//          if (F[n-1]==-1)
//             F[n-1] = fibo_m(n-1);

//         return F[n-2]+F[n-1];
//     }
// }

// int main(){
//     int n;
//     cout<<fibo_m(7);
// }

// better dynamic way of using cache(memoization/table) than above
int fib_dynamic(int n){
    int i;
    int cache[n];

    // creating table
    for (i=0; i<n; i++) cache[n] = -1;
    
    if (n <= 1) return n;

    if (cache[n] != -1) return cache[n];
    
    cache[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2);

    return cache[n];
}

int main(){
    int n;
    cout<<fib_dynamic(7);
}