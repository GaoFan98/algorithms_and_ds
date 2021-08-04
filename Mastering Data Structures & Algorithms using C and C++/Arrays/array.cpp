#include <iostream>
using namespace std;

struct Array
{
    int A[10];
    int size;
    int length;
};

void Display(struct Array arr)
{
    int i;
    printf("Array elements: \n");

    for (i = 0; i < arr.length; i++)
        printf("%d\n",arr.A[i]);
    
};

void Append(struct Array *arr, int x)
{
    if (arr->length<arr->size)
        arr->A[arr->length]=x;
        arr->length++;

        // or even simplier way
        // arr->A[arr->length++]=x;
}

void Insert(struct Array *arr, int index, int x)
{
    int i;

    if (index>=0 && arr->length>=index)
        for (i=arr->length; i>index; i--)
            arr->A[i]=arr->A[i-1];   
        

        arr->A[index]=x;
        arr->length++;
}

int Delete(struct Array *arr, int index)
{
    int i,x;

    if (index>=0 && index<arr->length)
        x = arr->A[index];

        for (i=index; i<arr->length-1; i++)
            arr->A[i]=arr->A[i+1];   
        
        arr->length--;
        
        return x;

    return 0;
}

int main()
{
    struct Array arr={{2,3,4,5,6},10,5};

    // Append(&arr,10);
    // Insert(&arr,3,2);
    Delete(&arr,0);
    Display(arr);

    return 0;
}

