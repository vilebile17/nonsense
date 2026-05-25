#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int *arr, int *result, size_t n) {
  for (int i = 0; i < n; i++) {
    result[i] = arr[i];
  }

  int flag = 1;
  while (flag) {
    flag = 0;
    for (int i = 0; i < n - 1; i++) {
      if (result[i] > result[i + 1]) {
        int temp = result[i];
        result[i] = result[i + 1];
        result[i + 1] = temp;
        flag = 1;
      }
    }
  }
}

void printArr(int *arr, size_t n) {
  printf("[");
  for (int i = 0; i < n; i++) {
    printf("%d", arr[i]);
    if (i != n - 1) {
      printf(",");
    }
  }
  printf("]\n");
}

int main() {
  int n = 5;
  int *arr = malloc(sizeof(int) * n);
  if (arr == NULL) {
    printf("there was an error creating the array");
    return 1;
  }

  arr[0] = 3;
  arr[1] = 2;
  arr[2] = 5;
  arr[3] = 1;
  arr[4] = 4;

  int *result = malloc(sizeof(int) * n);
  if (arr == NULL) {
    printf("there was an error creating the array");
    return 1;
  }

  bubbleSort(arr, result, n);
  printArr(result, n);

  return 0;
}
