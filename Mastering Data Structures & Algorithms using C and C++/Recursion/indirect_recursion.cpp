#include <iostream>
using namespace std;

// declaration of indirect_r_B, 
// if remove this, then next function will not find the function
void indirect_r_B(int n);

void indirect_r_A(int n){
    if (n>0)
    {
        cout<<n<<endl;
        indirect_r_B(n-1);
    }
}

void indirect_r_B(int n){
    if (n>1)
    {
        cout<<n<<endl;
        indirect_r_A(n/2);
    }
}

int main(){
    indirect_r_A(20);

    return 0;
}