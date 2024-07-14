from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def multiline_text():
    multiline_text = """
#include<stdio.h>
#include<sys/time.h>
#include<time.h>
#include<sys/resource.h>

void main()
{
 struct timeval  tv1, tv2;
int size,input[50],i; 
 struct rusage r_usage;

 printf("Enter the input size \n");
 scanf("%d",&size);
 printf("Enter the array elements \n");
 for(i=0;i<size;i++)
 {
  scanf("%d",&input[i]);
 }
gettimeofday(&tv1, NULL);
 selection_sort(input,size);
gettimeofday(&tv2, NULL);
 printf("\n Sorted array is \n");
 for(i=0;i<size;i++)
 {
  printf("%d\t",input[i]);
 }
 printf("Time of selection sort = %f microseconds",(double)(tv2.tv_usec-tv1.tv_usec));
//  printf ("Total time = %f seconds\n", (double) (tv2.tv_usec - tv1.tv_usec) / 1000000 +  (double) (tv2.tv_sec - tv1.tv_sec));
 getrusage(RUSAGE_SELF,&r_usage);
 printf("Memory usage: %ld kilobytes\n",r_usage.ru_maxrss);
}

void selection_sort(int input[100],int n)
{
 int i,j,min,temp;
 for(i=0;i<=n-2;i++)
 {
  min=i;
  for(j=i+1;j<=n-1;j++)
  {
   if(input[j]<input[min])
         min=j;
  }
    temp=input[min];
    input[min]=input[i];
    input[i]=temp;
  }
}




// Insertion sort

#include <stdio.h>

// Function to print an array
void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");
}

void insertionSort(int array[], int size) {
  for (int step = 1; step < size; step++) {
    int key = array[step];
    int j = step - 1;

    // Compare key with each element on the left of it until an element smaller than
    // it is found.
    // For descending order, change key<array[j] to key>array[j].
    while (key < array[j] && j >= 0) {
      array[j + 1] = array[j];
      --j;
    }
    array[j + 1] = key;
  }
}

// Driver code
int main() {
  int data[] = {9, 5, 1, 4, 3};
  int size = sizeof(data) / sizeof(data[0]);
  insertionSort(data, size);
  printf("Sorted array in ascending order:\n");
  printArray(data, size);
}
    """
return Response(multiline_text, mimetype='text/plain')

if name == 'main':
app.run(host='0.0.0.0', port=80)
