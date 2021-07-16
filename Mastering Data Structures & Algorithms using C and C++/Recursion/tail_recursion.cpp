#include <iostream>
using namespace std;

void tail_r(int k){
    if (k>0){
        cout << k << endl;
        tail_r(k-1);
    }
}

int main(){
    int x = 3;
    tail_r(x);

    return 0;
}