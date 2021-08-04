#include <iostream>
using namespace std;

struct Array
{
    int A[10];
    int size;
    int length;
};

int BinarySearch(struct Array arr, int find_int)
{
    int low, high, middle;

    low=0;
    high=arr.length-1;

    while (low<=high)
    {
        middle=(low+high)/2;

        if (find_int==arr.A[middle]) return middle;
        
        else if(find_int<arr.A[middle]) high=middle-1;
        
        else low=middle+1;
    }
    
    return -1;
}

int Recursive_BS(int arr[], int low,int high, int find_int)
{

    int middle;

    if (low<=high){
        middle=(low+high)/2;

        if (find_int==arr[middle]) return middle;
        
        else if(find_int<arr[middle]) return Recursive_BS(arr,low,middle-1,find_int);
        
        else return Recursive_BS(arr,middle+1,high,find_int);
    }
    
    return -1;
}

int main()
{
    struct Array arr={{2,3,4,5,6},10,5};

    printf("%d\n",BinarySearch(arr,6));
    printf("%d\n",Recursive_BS(arr.A,0,arr.length,3));

    return 0;
}