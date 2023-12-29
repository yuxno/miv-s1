
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
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));

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




////////////////////////sorted/////////////////////////////
void sorted(int *table, int n){
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
    }

 //////////////////////////////random/////////////////////////////////
void random(int *table, int n){

    for (int i = 0; i < n; i++) {
        table[i] = rand() % 1000;
    }
    }


 /////////////////////////reversed/////////////////////////////////

void reversed(int *table, int n){
  table[0] = rand() % 1000;

    for (int i = 1; i < n; i++) {
        int valueToInsert = rand() % 1000;

        int j = i - 1;
        while (j >= 0 && table[j] < valueToInsert) {
            table[j + 1] = table[j];
            j--;
        }

        table[j + 1] = valueToInsert;
    }
    }

    //////////////////////////////////////////////////////////////////
/*int main(){

    int n = 8 * 10000;
    int k;
    int *table = (int *)malloc(n * sizeof(int));


    srand(time(NULL));





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


int main() {
    srand(time(NULL));

    clock_t start_time, end_time;
    double cpu_time_used;

    int sort_type;
    printf("Choose a sort algorithm:\n1: Insertion Sort\n2: Bubble Sort\n3: Merge Sort\n4: Quick Sort\n5: Heap Sort\n");
    scanf("%d", &sort_type);

        int array_size = 8 * 10000;
        int *table = (int *)malloc(array_size * sizeof(int));

        printf("\n");






            switch(sort_type) {
                case 1:
                    printf("\nUsing Insertion Sort...\n");


                        //boucle for defirante array size
                        printf("\nFilling Sorted Array...\n");
                        sorted(table, array_size);
                        start_time = clock();
                        insertionSort(table, array_size);
                        end_time = clock();
                        cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
                        printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                        free(table);


                        printf("\nFilling Random Array...\n");
                        random(table, array_size);
                        start_time = clock();
                        insertionSort(table, array_size);
                        end_time = clock();
                        cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
                        printf("Execution Time for fill type 2: %f seconds\n", cpu_time_used);
                        free(table);


                        printf("\nFilling Reversed Array...\n");
                        reversed(table, array_size);
                        start_time = clock();
                        insertionSort(table, array_size);
                        end_time = clock();
                        cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
                        printf("Execution Time for fill type 3: %f seconds\n", cpu_time_used);
                        free(table);

                    break;



                case 2:
                    bubbleSort(table, array_size);
                    break;
                case 3:
                    arraySplit(table, 0, array_size - 1);
                    break;
                case 4:
                    quickSort(table, 0, array_size - 1);
                    break;
                case 5:
                    heapSort(table, array_size);
                    break;

            }


            printf("THE END...\n");





    return 0;
}




void testSortAlgorithm(int sort_type, int array_size) {
    int *table;
    free(table);
    table = (int *)malloc(array_size * sizeof(int));

    printf("\n");

    switch (sort_type) {
        case 1:
            printf("\nUsing Insertion Sort...\n");


                        //boucle for defirante array size
                        printf("\nFilling Sorted Array...\n");
                        sorted(table, array_size);
                        clock_t start_time = clock();
                        insertionSort(table, array_size);
                        clock_t end_time = clock();
                        double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
                        printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                        free(table);


                        printf("\nFilling Random Array...\n");
                        random(table, array_size);
                        start_time = clock();
                        insertionSort(table, array_size);
                        end_time = clock();
                        cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
                        printf("Execution Time for fill type 2: %f seconds\n", cpu_time_used);
                        free(table);


                        printf("\nFilling Reversed Array...\n");
                        reversed(table, array_size);
                        start_time = clock();
                        insertionSort(table, array_size);
                        end_time = clock();
                        cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
                        printf("Execution Time for fill type 3: %f seconds\n", cpu_time_used);
                        free(table);
            break;
        case 2:
            bubbleSort(table, array_size);
            break;
        case 3:
            bubbleSort(table, array_size);
            break;
        case 4:
            bubbleSort(table, array_size);
            break;
        case 5:
            bubbleSort(table, array_size);
            break;

    }
    free(table);
}

int main() {
    srand(time(NULL));
    clock_t start_time, end_time;
    double cpu_time_used;

    int sort_type;
    printf("Choose a sort algorithm:\n1: Insertion Sort\n2: Bubble Sort\n3: Merge Sort\n4: Quick Sort\n5: Heap Sort\n");
    scanf("%d", &sort_type);

    // Tableau des tailles à tester
    int sizes[] = {5 * 10000, 100000, 2 * 100000, 4 * 100000, 8 * 100000, 16 * 2 * 100000, 32 * 2 * 100000, 64 * 100000, 128 * 100000, 256 * 100000, 512 * 100000, 1024 * 100000, 2048 * 100000};
    for (int i = 0; i < sizeof(sizes) / sizeof(sizes[0]); ++i) {
        int array_size = sizes[i];
        printf("\nArray Size: %d\n", array_size);
        testSortAlgorithm(sort_type, array_size);
    }





    return 0;
}
*/


void testSortAlgorithm(int sort_type, int array_size, int fill_type) {
    int *table = (int *)malloc(array_size * sizeof(int));

    printf("\n");

    switch (sort_type) {
        case 1:
            printf("\nUsing Insertion Sort...\n");
            switch (fill_type)
            {
            case 1:
            printf("\nFilling Sorted Array...\n");
            sorted(table, array_size);
            clock_t start_time = clock();
            insertionSort(table, array_size);
            clock_t end_time = clock();
            double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 2:
            printf("\nFilling reversed Array...\n");
            reversed(table, array_size);
            start_time = clock();
            insertionSort(table, array_size);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 3:
            printf("\nFilling random Array...\n");
            random(table, array_size);
            start_time = clock();
            insertionSort(table, array_size);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
            default:
            printf("Invalid choice\n");
                break;
            }

            break;
        case 2:
            printf("\nUsing bubble Sort...\n");
            switch (fill_type)
            {
            case 1:
            printf("\nFilling Sorted Array...\n");
            sorted(table, array_size);
            clock_t start_time = clock();
            bubbleSort(table, array_size);
            clock_t end_time = clock();
            double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 2:
            printf("\nFilling reversed Array...\n");
            reversed(table, array_size);
            start_time = clock();
            bubbleSort(table, array_size);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 3:
            printf("\nFilling random Array...\n");
            random(table, array_size);
            start_time = clock();
            bubbleSort(table, array_size);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
            default:
            printf("Invalid choice\n");
                break;
            }
            break;
        case 3:
                    printf("\nUsing merge Sort...\n");
            switch (fill_type)
            {
            case 1:
            printf("\nFilling Sorted Array...\n");
            sorted(table, array_size);
            clock_t start_time = clock();
            arraySplit(table,0,array_size-1);
            clock_t end_time = clock();
            double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 2:
            printf("\nFilling reversed Array...\n");
            reversed(table, array_size);
            start_time = clock();
            arraySplit(table,0,array_size-1);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 3:
            printf("\nFilling random Array...\n");
            random(table, array_size);
            start_time = clock();
            arraySplit(table,0,array_size-1);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
            default:
            printf("Invalid choice\n");
                break;
            }
            break;
        case 4:
                    printf("\nUsing quick Sort...\n");
            switch (fill_type)
            {
            case 1:
            printf("\nFilling Sorted Array...\n");
            sorted(table, array_size);
            clock_t start_time = clock();
            quickSort(table,0, array_size-1);
            clock_t end_time = clock();
            double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 2:
            printf("\nFilling reversed Array...\n");
            reversed(table, array_size);
            start_time = clock();
            quickSort(table,0, array_size-1);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 3:
            printf("\nFilling random Array...\n");
            random(table, array_size);
            start_time = clock();
            quickSort(table,0, array_size-1);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
            default:
            printf("Invalid choice\n");
                break;
            }
            break;
        case 5:
            printf("\nUsing heap Sort...\n");
            switch (fill_type)
            {
            case 1:
            printf("\nFilling Sorted Array...\n");
            sorted(table, array_size);
            clock_t start_time = clock();
            heapSort(table, array_size);
            clock_t end_time = clock();
            double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 2:
            printf("\nFilling reversed Array...\n");
            reversed(table, array_size);
            start_time = clock();
            heapSort(table, array_size);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
                break;
            case 3:
            printf("\nFilling random Array...\n");
            random(table, array_size);
            start_time = clock();
            heapSort(table, array_size);
            end_time = clock();
            cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
            printf("Execution Time for fill type 1: %f seconds\n", cpu_time_used);
            default:
            printf("Invalid choice\n");
                break;
            }
            break;
        default:
            printf("Invalid choice\n");
            free(table);
            return;
    }

    free(table); // Move this line outside the switch statement
}

int main() {

    srand(time(NULL));
    int sort_type;
    int fill_type;
    printf("Choose a sort algorithm:\n1: Insertion Sort\n2: Bubble Sort\n3: Merge Sort\n4: Quick Sort\n5: Heap Sort\n");
    scanf("%d", &sort_type);

    printf("Choose a fillin method:\n1: sorted\n2: reversed\n3: random\n");
    scanf("%d", &fill_type);

    int sizes[] = {5 * 10000, 100000, 2 * 100000, 4 * 100000, 8 * 100000, 16 * 100000, 32 * 100000, 64 * 100000, 128 * 100000, 256 * 100000, 512 * 100000, 1024 * 100000, 2048 * 100000};/*, 16 * 2 * 100000, 32 * 2 * 100000, 64 * 100000, 128 * 100000, 256 * 100000, 512 * 100000, 1024 * 100000, 2048 * 100000};*/

    for (int i = 0; i < sizeof(sizes) / sizeof(sizes[0]); ++i) {
        int array_size = sizes[i];
        printf("\nArray Size: %d\n", array_size);
        testSortAlgorithm(sort_type, array_size,fill_type);
    }

    return 0;
}
