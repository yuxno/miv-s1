/*#include <stdio.h>
#include <stdlib.h>


/*
int main()
{
    //tri par insertion
    /*
   int table[]={5,6,2,3,7,4,1,9};
   int i,j,k,s,n=8;
   for(i=0;i<n;i++){
       s=table[i+1];
       k=i+1;
       for(j=i;j>=0;j--){
        if(table[j]>table[k]){
            table[k]=table[j];
            table[j]=s;
            k--;
        }
       }
       }
*/
/*
//bull algo
int table[]={5,6,2,3,7,4,1,9};
int i,n=8,k=0,s;
printf("the old table is:\n");

for(i=0;i<n;i++){
    printf("%d \n", table[i]);
}
while (k<n-1){

for(i=0;i<n;i++){
    if(table[i]>table[i+1]){
        s=table[i+1];
        table[i+1]=table[i];
        table[i]=s;
        k=0;
    }else k++;
}
}


printf("the new table is:\n");

for(i=0;i<n;i++){
    printf("%d", table[i]);

}
*/



//fusion
/*

void merge(int tab[], int l, int r, int m){

        int left_size=m-l+1;
        int right_size=r-m;

        int arr1[left_size];
        int arr2[right_size];

        int i,j,k=l;
        i=j=0;

        for (i=0;i<left_size;i++)
            arr1[i]=tab[i+l];

        for(i=0;i<right_size;i++)
            arr2[i]=tab[i+m+1];


        while(i<left_size && j<right_size){

            if(arr1[i]<=arr2[j])
            {
                tab[k]=arr1[i];
                i++;
            }else{
                tab[k]=arr2[j];
                j++;
            }
            k++;
        }

        while(i<left_size){
            tab[k]=arr1[i];
                i++;
                k++;
        }

         while(j<right_size){
            tab[k]=arr2[j];
                j++;
                k++;
        }


            /*
        for(i=0,j=0,k=l;k<r;k++){

            if((i<left_size) && (j>=right_size || arr1[i]<=arr2[j])){
                tab[k]=arr1[i];
                i++;
            }else{
                tab[k]=arr2[j];
                j++;
            }


        }*/
/*


void splitArray(int tab[], int l,int r){

    int m;
    if(l<r){
          m = l + (r - l) / 2;
        splitArray(tab,l,m);
        splitArray(tab,m+1,r);

        merge(tab,l,r,m);
    }

}


void printArray(int A[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		printf("%d ", A[i]);
	printf("\n");
}


int main(){

int tab[]={5,6,1,2,8,4,3,7};
int size=8;
printf("the first array is: \n");

printArray(tab,size);
int l=0; int r=size-1;
splitArray(tab,l,r);

printf("the new array is \n");
printArray(tab,size);
return 0;

}
*/
/*

void merge(int arr[], int l, int m, int r)
{
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
		}
		else {
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


void arraySplit(int arr[], int l, int r)
{
	if (l < r) {
		int m = l + (r - l) / 2;

		arraySplit(arr, l, m);
		arraySplit(arr, m + 1, r);

		merge(arr, l, m, r);
	}
}


void printArray(int A[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		printf("%d ", A[i]);
	printf("\n");
}

int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int arr_size = 6;

	printf("original array is \n");
	printArray(arr, arr_size);

	arraySplit(arr, 0, arr_size - 1);

	printf("new array is \n");
	printArray(arr, arr_size);
	return 0;
}

*/



//quick sort
/*
so uh here u compare the table elements with the pivot, aka the last element,
then u put the elments that are > than the pivot u place em after it
then pick the pivot outa the 2 new lists (less n big than old pivot)
*/
/*

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
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


void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = 6;

    printf("Original array: \n ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    quickSort(arr, 0, n - 1);

    printf("new array:\n ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}

*/

// heap sort
/*
basically here you convert your array to a binary tree, and you change it each time as
in the root should be bigger than its children, so you swap between the elements, and each time u get
to the biggest room u delete it n replace it with the last node, they u sort it again , each time delete the biggest elm
untill ur done */
/*

void swap(int* a, int* b)
{

	int temp = *a;
	*a = *b;
	*b = temp;
}

void heapify(int arr[], int N, int i)
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


void heapSort(int arr[], int N)
{

	for (int i = N / 2 - 1; i >= 0; i--)

		heapify(arr, N, i);
	for (int i = N - 1; i >= 0; i--) {
		swap(&arr[0], &arr[i]);
		heapify(arr, i, 0);
	}
}


void printArray(int arr[], int N)
{
	for (int i = 0; i < N; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int N = sizeof(arr) / sizeof(arr[0]);

    printf("og array is \n");
    printArray(arr,N);

	heapSort(arr, N);
	printf("Sorted array is\n");
	printArray(arr, N);
}

*/

