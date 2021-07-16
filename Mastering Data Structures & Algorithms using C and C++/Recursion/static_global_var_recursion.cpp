#include <iostream>
using namespace std;

// static variables in recursion
int static_r(int s){
    static int counter=0;

    if (s>0){
        counter++;
        return static_r(s-1)+counter;
    }
    return 0;
}

// global variables in recursion
int gl=0;

int global_r(int g){
    if (g>0){
        gl++;
        return global_r(g-1)+gl;
    }
    return 0;
}

int main(){
    int r=2;
    int l=2;

    r=static_r(r);
    cout << r << endl;

    l=global_r(l);
    cout << l <<endl;

    return 0;
}