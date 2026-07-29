#include <stdio.h>
#include <stdlib.h>

int longest_increasing_subsequence(int *arr, int n) {
  int current_subsequence_length = 1;
  int longest_subsequence_length = 1;

  for (int i = 1; i < n; i++) {
    if (arr[i] > arr[i - 1]) {
      current_subsequence_length++;
    } else {
      if (current_subsequence_length > longest_subsequence_length) {
        longest_subsequence_length = current_subsequence_length;
      }
      current_subsequence_length = 1;
    }
    printf("Current subsequence length is %d\n", current_subsequence_length);
  }

  if (current_subsequence_length > longest_subsequence_length) {
    longest_subsequence_length = current_subsequence_length;
  }
  return longest_subsequence_length;
}

int main() {
  int n = 7;
  int *arr = malloc(sizeof(int) * n);
  if (arr == NULL) {
    printf("there was an error creating the array\n");
    return 1;
  }
  arr[0] = 1;
  arr[1] = 2;
  arr[2] = 0;
  arr[3] = 3;
  arr[4] = 6;
  arr[5] = 7;
  arr[6] = 8;

  printf("The result is %d\n", longest_increasing_subsequence(arr, n));
  return 0;
}
