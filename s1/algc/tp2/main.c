#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include<windows.h>


void toursDeHanoi(int n, char A, char B, char C) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", A, C);
        return;
    }

    toursDeHanoi(n - 1, A, C, B);
    printf("Move disk %d from %c to %c\n", n, A, C);
    toursDeHanoi(n - 1, B, A, C);
}

int main() {
    int n;

    clock_t start_time, end_time;
    double cpu_time_used;


    //printf("Enter the number of disks: ");
    //scanf("%d", &n);

    for (n=22;n<=40;n++)
    {
    start_time = clock();

    toursDeHanoi(n, 'A', 'B', 'C');

    end_time = clock();
    cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("\n \n \n");

    printf("Execution Time: %f seconds for n= %d \n", cpu_time_used, n);



    printf("\n \n \n");

    sleep(10);



    }
    return 0;
}
