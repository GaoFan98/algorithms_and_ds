#include <iostream>
using namespace std;

void head_r(int n){
    if (n>0){
        head_r(n-1);
        cout << n << endl;
    }
}

int main(){
    int x = 3;
    head_r(x);

    return 0;
}