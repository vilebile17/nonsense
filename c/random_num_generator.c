#include "math.h"
#include "stdio.h"
#include "stdlib.h"

// Wikipedia page: https://en.wikipedia.org/wiki/Lehmer_random_number_generator
// Prime numbers page: https://www.mathematical.com/primes0to1000k.html

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("USAGE: random_num_generator <seed>\n");
    return 1;
  }

  int a = pow(7, 5);
  int m = 9973;
  int seed = atoi(argv[1]);
  printf("%d\n", (a * seed) % m);
  return 0;
}
