#include <iostream>
using namespace std;

int nested_r(int n){
    if (n>100){
        return n-10;
    }
    
    return nested_r(nested_r(n+11));
}

int main(){
    int r;
    r = nested_r(95);
    cout<<r;

    return 0;
}