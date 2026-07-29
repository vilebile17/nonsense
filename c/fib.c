#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void reverse_string(char *dest, char *src) {
  size_t len = strlen(src);

  for (size_t i = 0; i < len; i++) {
    dest[i] = src[len - 1 - i];
  }

  dest[len] = '\0';
}

void add_string(char *s1, char *s2, char *dest) {
  int i = 0;
  size_t str1len = strlen(s1);
  size_t str2len = strlen(s2);
  int carry = 0;

  char *str1 = malloc((str1len + 1) * sizeof(char));
  char *str2 = malloc((str2len + 1) * sizeof(char));

  if (str1 == NULL || str2 == NULL) {
    printf("an error occured when allocating the memory");
    exit(1);
  }

  reverse_string(str1, s1);
  reverse_string(str2, s2);

  while (i < str1len || i < str2len || carry == 1) {
    int res = carry;

    if (i < str1len) {
      res += str1[i] - '0';
    }

    if (i < str2len) {
      res += str2[i] - '0';
    }

    if (res > 9) {
      carry = 1;
      res -= 10;
    } else {
      carry = 0;
    }

    dest[i] = res + '0';
    i++;
  }

  free(str1);
  free(str2);

  dest[i] = '\0';
  char dst_copy[strlen(dest) + 1];
  strcpy(dst_copy, dest);
  reverse_string(dest, dst_copy);
}

int count_threes(char *num) {
  int count = 0;
  for (size_t i = 0; i < strlen(num); i++) {
    if (num[i] == '3') {
      count++;
    }
  }
  return count;
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("USAGE: %s <num>\n", argv[0]);
    return 1;
  } 

  int iterations = atoi(argv[1]) - 2;

  int buffer_size = 0.25 * iterations + 2;

  char a[buffer_size];
  char b[buffer_size];
  char c[buffer_size];
  int three_count = 0;

  a[0] = '0';
  a[1] = '\0';
  b[0] = '1';
  b[1] = '\0';

  if (iterations > -2) {
    printf("%s\n", a);
  }
  if (iterations > -1) {
    printf("%s\n", b);
  }

  for (int i = 0; i < iterations; i++) {
    add_string(a, b, c);

    strcpy(a, b);
    strcpy(b, c);

    if (i < 98) {
      printf("%s\n", b);
    } else if (i == 98) {
      printf("...\n");
    }
    three_count += count_threes(b);
  }

  
  printf("\n");
  printf("In total, there were %d threes\n", three_count);
  printf("We chose a buffer size of %d bytes\n", buffer_size);

  return 0;
}
