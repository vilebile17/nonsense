#include <stdio.h>

double epicSqrt(double S) {
  if (S == 0.0) {
    return 0.0;
  } else if (S == 1.0) {
    return 1.0;
  }

  // As wikipedia puts it: "if x is an overestimate, then S/x will be an
  // underestimate and vice-versa. Therefore, it is reasonable to assume that
  // the mean of the two numbers will be a better approximation for the value."
  // - https://en.wikipedia.org/wiki/Square_root_algorithms#Derivation
  // Therefore we just find the mean over and over again

  double x = S / 2.0;
  for (int i = 0; i < 10; i++) {
    x = (1.0 / 2.0) * (x + S / x);
  }
  return x;
}

int main() {
  double n;
  while (1) {
    printf("Enter a number to square root: ");
    scanf("%lf", &n);

    if (n >= 0) {
      double val = epicSqrt(n);
      printf("The square root of %.3f is %.3f\n", n, val);
    } else { // complex square roots
      double val = epicSqrt(n * -1.0);
      printf("The square root of %.3f is %.3fi\n", n, val);
    }
  }
  return 0;
}
