#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_SIZE 10000
#define STEP_SIZE 1000
#define NUM_ALGORITHMS 4

// Function prototypes
void bubbleSort(int arr[], int n);
void insertionSort(int arr[], int n);
void selectionSort(int arr[], int n);
void quickSort(int arr[], int n);
void quickSortHelper(int arr[], int low, int high);
int partition(int arr[], int low, int high);
void generateRandomArray(int arr[], int n);
void copyArray(int src[], int dest[], int n);
double measureSortingTime(void (*sortFunction)(int[], int), int arr[], int n);

int main() {
    FILE *dataFile;
    dataFile = fopen("sorting_data.txt", "w");
    if (dataFile == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    srand(time(NULL));

    fprintf(dataFile, "Size BubbleSort InsertionSort SelectionSort QuickSort\n");

    for (int size = STEP_SIZE; size <= MAX_SIZE; size += STEP_SIZE) {
        int originalArray[MAX_SIZE];
        int tempArray[MAX_SIZE];
        
        generateRandomArray(originalArray, size);

        // Measure Bubble Sort
        copyArray(originalArray, tempArray, size);
        double bubbleTime = measureSortingTime(bubbleSort, tempArray, size);

        // Measure Insertion Sort
        copyArray(originalArray, tempArray, size);
        double insertionTime = measureSortingTime(insertionSort, tempArray, size);

        // Measure Selection Sort
        copyArray(originalArray, tempArray, size);
        double selectionTime = measureSortingTime(selectionSort, tempArray, size);

        // Measure Quick Sort
        copyArray(originalArray, tempArray, size);
        double quickTime = measureSortingTime(quickSort, tempArray, size);

        fprintf(dataFile, "%d %f %f %f %f\n", size, bubbleTime, insertionTime, selectionTime, quickTime);
    }

    fclose(dataFile);

    // Generate gnuplot script
    FILE *gnuplotScript = fopen("plot_script.gp", "w");
    if (gnuplotScript == NULL) {
        printf("Error opening gnuplot script file!\n");
        return 1;
    }

    fprintf(gnuplotScript, "set title 'Sorting Algorithm Performance'\n");
    fprintf(gnuplotScript, "set xlabel 'Array Size'\n");
    fprintf(gnuplotScript, "set ylabel 'Time (seconds)'\n");
    fprintf(gnuplotScript, "set key outside\n");
    fprintf(gnuplotScript, "plot 'sorting_data.txt' using 1:2 with lines title 'Bubble Sort', \
                                 '' using 1:3 with lines title 'Insertion Sort', \
                                 '' using 1:4 with lines title 'Selection Sort', \
                                 '' using 1:5 with lines title 'Quick Sort'\n");
    fprintf(gnuplotScript, "pause -1\n");

    fclose(gnuplotScript);

    // Execute gnuplot script
    system("gnuplot plot_script.gp");

    return 0;
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

void quickSort(int arr[], int n) {
    quickSortHelper(arr, 0, n - 1);
}

void quickSortHelper(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortHelper(arr, low, pi - 1);
        quickSortHelper(arr, pi + 1, high);
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}

void generateRandomArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }
}

void copyArray(int src[], int dest[], int n) {
    memcpy(dest, src, n * sizeof(int));
}

double measureSortingTime(void (*sortFunction)(int[], int), int arr[], int n) {
    clock_t start, end;
    start = clock();
    
    sortFunction(arr, n);
    
    end = clock();
    return ((double)(end - start)) / CLOCKS_PER_SEC;
}