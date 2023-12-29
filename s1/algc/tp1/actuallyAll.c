
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

///////////////////////////insertion//////////////////////////

void insertionSort(int *arr, int n) {
    int i, j, key;

    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        arr[j + 1] = key;
    }
}

///////////////////////////////////bubbles//////////////////////////

void bubbleSort(int *arr, int n)
{
    int k=0;
    int s,i;
//printf("annyong");

    while (k<n-1){

    for(i=0;i<n;i++){
        if(arr[i]>arr[i+1]){
            s=arr[i+1];
            arr[i+1]=arr[i];
            arr[i]=s;
            k=0;
        }else k++;
    }
    }
}

///////////////////////////////////merge/////////////////////////////

void mergeSort(int *arr, int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void arraySplit(int *arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        arraySplit(arr, l, m);
        arraySplit(arr, m + 1, r);

        mergeSort(arr, l, m, r);
    }
}

//////////////quick sort///////////////

    void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int *arr, int low, int high) {
    int pivot = arr[high];
    int i = (low - 1); //so that itd be on the left side of the pivot

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}


void quickSort(int *arr,int low, int high)
{
    //printf("annyong");

     if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

//////////////////////////////////////////heap//////////////////////////////////





void heapify(int *arr, int N, int i)
{

	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;
	if (left < N && arr[left] > arr[largest])

		largest = left;
	if (right < N && arr[right] > arr[largest])

		largest = right;

	if (largest != i) {

		swap(&arr[i], &arr[largest]);
		heapify(arr, N, largest);
	}
}


void heapSort(int *arr, int N)
{

	for (int i = N / 2 - 1; i >= 0; i--)

		heapify(arr, N, i);
	for (int i = N - 1; i >= 0; i--) {
		swap(&arr[0], &arr[i]);
		heapify(arr, i, 0);
	}
}




int main(){

    int n = 8 * 100000;
    int k;
    int *table = (int *)malloc(n * sizeof(int));


    srand(time(NULL));

  ////////////////////////sorted/////////////////////////////

    table[0] = rand() % 1000;
    for (int i = 1; i < n; i++) {
        int valueToInsert = rand() % 1000;

        int j = i - 1;
        while (j >= 0 && table[j] > valueToInsert) {
            table[j + 1] = table[j];
            j--;
        }
        table[j + 1] = valueToInsert;
    }

    //////////////////////////random//////////////////////
    /*

    for (int i = 0; i < n; i++) {
        table[i] = rand() % 1000;
    }*/


    /////////////////////////reversed/////////////////////////////////


  /*  table[0] = rand() % 1000;

    for (int i = 1; i < n; i++) {
        int valueToInsert = rand() % 1000;

        int j = i - 1;
        while (j >= 0 && table[j] < valueToInsert) {
            table[j + 1] = table[j];
            j--;
        }

        table[j + 1] = valueToInsert;
    }*/

    //////////////////////////////////////////////////////////////////

    clock_t start_time, end_time;
    double cpu_time_used;

    printf("which sort algorithm you wish to perform \n 1:insertion sort \n 2:bubble sort \n 3:merge \n 4:quick sort \n 5:heap sort \n");
    scanf("%d", &k);

    start_time = clock();

    switch(k){
        case 1:
            printf("you chose insertion sort \n");
            insertionSort(table,n);
            break;
        case 2:
             printf("you chose bubble sort \n");
            bubbleSort(table,n);
            break;
        case 3:
             printf("you chose merge sort \n");
            arraySplit(table, 0, n-1);

            break;
        case 4:
             printf("you chose quick sort \n");
             quickSort(table, 0, n - 1);
            break;
        case 5:
             printf("you chose heap sort \n");
            heapSort(table,n);
            break;


    }


    end_time = clock();
    cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Execution Time: %f seconds\n", cpu_time_used);

    free(table); // Free dynamically allocated memory

    return 0;

}

