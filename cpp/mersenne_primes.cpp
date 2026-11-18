#include <cmath>
#include <iostream>

bool is_prime(int num) {
  if (num == 1 || num == 0) {
    return false;
  } else if (num == 2) {
    return true;
  }

  for (int i = 2; i * i <= num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
  int i = 1;
  while (true) {
    if (is_prime(std::pow(2, i) - 1)) {
      std::cout << "2^" << i << " - 1 is prime!" << "\n";
    }
    i++;
  }
  return 0;
}
