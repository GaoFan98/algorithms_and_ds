#include <iostream>
using namespace std;

struct Array
{
    int *A;
    int size;
    int length;
};

void Display(struct Array arr)
{
    int i;
    printf("Elements \n");

    for (i = 0; i < arr.length; i++)
    {
        printf("%d",arr.A[i]);
    }
};

int main()
{
    struct  Array arr;
    int n,i;

    printf("Size of an array");
    scanf("%d",&arr.size);

    // allocate the memory for an array taken from input
    arr.A=(int *)malloc(arr.size*sizeof(int));
    // initial setup length of array to zero
    arr.length=0;

    printf("Enter number of integers in array");
    scanf("%d",&n);
    // allocating all the integers to array from input 
    for (i=0; i<n; i++){
        scanf("%d",&arr.A[i]);
    }

    // assigning the length from the input
    arr.length=n;

    Display(arr);
}
