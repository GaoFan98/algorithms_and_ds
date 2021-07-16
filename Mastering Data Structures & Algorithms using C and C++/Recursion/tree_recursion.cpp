#include <iostream>
using namespace std;

void tree_r(int x){
    if (x>0)
    {
        cout<<x<<endl;
        tree_r(x-1);
        tree_r(x-1);
    }
    
}

int main(){
    tree_r(3);

    return 0;
}