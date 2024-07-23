#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(&arr[j], &arr[j+1]);
            }
        }
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void selectionSort(int arr[], int n) {
    int min_idx;
    for (int i = 0; i < n-1; i++) {
        min_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        swap(&arr[min_idx], &arr[i]);
    }
}

void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}

void merge(int arr[], int l, int m, int r) {
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

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

int getMax(int arr[], int n) {
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}

void countSort(int arr[], int n, int exp) {
    int output[n];
    int i, count[10] = {0};

    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    for (i = 0; i < n; i++)
        arr[i] = output[i];
}

void radixSort(int arr[], int n) {
    int m = getMax(arr, n);

    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp);
}

int main() {
    int arr[10000];
    int n = sizeof(arr) / sizeof(arr[0]);

    // Initialize array with random numbers
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }

    clock_t start, end;
    double elapsedTime;

    // Measure time for Bubble Sort
    int bubbleSortArray[n];
    for (int i = 0; i < n; i++) {
        bubbleSortArray[i] = arr[i];
    }
    start = clock();
    bubbleSort(bubbleSortArray, n);
    end = clock();
    elapsedTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Bubble Sort Time: %.6f seconds\n", elapsedTime);

    // Measure time for Quick Sort
    int quickSortArray[n];
    for (int i = 0; i < n; i++) {
        quickSortArray[i] = arr[i];
    }
    start = clock();
    quickSort(quickSortArray, 0, n-1);
    end = clock();
    elapsedTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Quick Sort Time: %.6f seconds\n", elapsedTime);

    // Measure time for Selection Sort
    int selectionSortArray[n];
    for (int i = 0; i < n; i++) {
        selectionSortArray[i] = arr[i];
    }
    start = clock();
    selectionSort(selectionSortArray, n);
    end = clock();
    elapsedTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Selection Sort Time: %.6f seconds\n", elapsedTime);

    // Measure time for Heap Sort
    int heapSortArray[n];
    for (int i = 0; i < n; i++) {
        heapSortArray[i] = arr[i];
    }
    start = clock();
    heapSort(heapSortArray, n);
    end = clock();
    elapsedTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Heap Sort Time: %.6f seconds\n", elapsedTime);

    // Measure time for Merge Sort
    int mergeSortArray[n];
    for (int i = 0; i < n; i++) {
        mergeSortArray[i] = arr[i];
    }
    start = clock();
    mergeSort(mergeSortArray, 0, n-1);
    end = clock();
    elapsedTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Merge Sort Time: %.6f seconds\n", elapsedTime);

    // Measure time for Radix Sort
    int radixSortArray[n];
    for (int i = 0; i < n; i++) {
        radixSortArray[i] = arr[i];
    }
    start = clock();
    radixSort(radixSortArray, n);
    end = clock();
    elapsedTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Radix Sort Time: %.6f seconds\n", elapsedTime);

    return 0;
}
