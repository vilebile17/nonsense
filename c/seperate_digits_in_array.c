#include <stdio.h>
#include <stdlib.h>

int *separateDigits(int *nums, int numsSize, int *returnSize) {
  int rs = 0;
  for (int i = 0; i < numsSize; i++) {
    int hasActivated = 0;
    int currentNum = nums[i];
    for (int divisor = 100000; divisor != 0; divisor /= 10) {
      if (nums[i] / divisor != 0 || hasActivated == 1) {
        int temp = currentNum / divisor;
        currentNum -= (temp * divisor);
        hasActivated = 1;
        rs++;
      }
    }
  }

  *returnSize = rs;
  int *answer = malloc(sizeof(int) * rs);
  if (answer == NULL) {
    printf("An error occured when allocating memory\n");
    exit(1);
  }

  int i = 0;
  for (int j = 0; j < numsSize; j++) {
    int hasActivated = 0;
    int currentNum = nums[j];
    for (int divisor = 100000; divisor != 0; divisor /= 10) {
      if (nums[j] / divisor != 0 || hasActivated == 1) {
        answer[i] = currentNum / divisor;
        currentNum -= (answer[i] * divisor);
        hasActivated = 1;
        i++;
      }
    }
  }

  return answer;
}

int main() {
  int *test = malloc(sizeof(int) * 4);
  if (test == NULL) {
    printf("An error occured when allocating memory\n");
    exit(1);
  }
  test[0] = 5000;
  test[1] = 1;
  test[2] = 3;
  test[3] = 9;

  int rs;
  int *answer = separateDigits(test, 4, &rs);

  printf("[");
  for (int i = 0; i < rs; i++) {
    printf("%d", answer[i]);
    if (i != rs - 1) {
      printf(", ");
    }
  }
  printf("]\n");
}
