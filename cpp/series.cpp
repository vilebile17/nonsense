#include <cmath>
#include <iostream>

int main() {
  int x;
  std::cout << "x -> ";
  std::cin >> x;
  int iterations;
  std::cout << "iterations -> ";
  std::cin >> iterations;

  float acc = 0;
  for (int i = 1; i < iterations; i++) {
    int sign = (i % 2);
    float cur = std::pow(x, -i);
    std::cout << cur << "\n";
    acc += sign * cur;
  }
  std::cout << "Final result: " << acc << "\n";
  return 0;
}
