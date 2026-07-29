#include <iostream>

int main() {
  int a = 1;
  int b = 1;
  const int iterations = 50;
  std::cout << a;
  std::cout << "\n";
  std::cout << b;
  std::cout << "\n";
  for (int i = 0; i < iterations; i++) {
    int c = a + b;
    a = b;
    b = c;
    std::cout << c;
    std::cout << "\n";
  }
}
