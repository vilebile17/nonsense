#include <stdio.h>
#include <stdlib.h>

int isPalindrome(int x) {
  int numDigits = 0;
  int result = x;
  while (result != 0) {
    result = result / 10;
    numDigits++;
  }

  if (x < 0) {
    numDigits++;
  }

  char *str = malloc(numDigits * sizeof(char));
  if (str == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1);
  }
  sprintf(str, "%d", x);

  for (int i = 0; i < numDigits / 2; i++) {
    if (str[i] != str[numDigits - i - 1]) {
      free(str);
      return 0;
    }
  }

  free(str);
  return 1;
}

int main() {
  int *tests = malloc(5 * sizeof(int));
  if (tests == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1);
  }

  tests[0] = 121;
  tests[1] = 120;
  tests[2] = 66;
  tests[3] = 1991;
  tests[4] = 1;

  for (int i = 0; i < 5; i++) {
    printf("Is the number %d a palindrome? ", tests[i]);
    if (isPalindrome(tests[i])) {
      printf("Yes it is!\n");
    } else {
      printf("No it's not :(\n");
    }
  }

  free(tests);
  return 0;
}
