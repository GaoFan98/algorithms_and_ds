#include <iostream>
using namespace std;

// recursion method O(n**2)
// double taylor_series(int x, int power){
//   static double perm_pow=1, fctr=1;
//   double result;

//   if(power==0){
//       return 1;
//   }

//     result = taylor_series(x,power-1);
//     perm_pow*=x;
//     fctr*=power;

//     return result+perm_pow/fctr;
// }

// int main(){
//     cout<<taylor_series(1,10);
// }

// loop
// double loop_ts(int x, int power){
//     double s=1;

//     for (; power>0;power--)
//     {
//         s=1+x*s/power;
//     }

//     return s;
// }

// int main(){
//     cout<<loop_ts(1,10);
// }

// Horner's Rule O(n)
// e**x=1+x/1(1+x/2(1+x/3(1+x/4)))
double horner_ts(int x, int power){
    static double s=1;

    if (power==0)
    {
        return s;
    }
    s=1+x*s/power;

    return horner_ts(x,power-1);
}

int main(){
    int x;
    int power;

    cout<<horner_ts(x=1,power=10);
}