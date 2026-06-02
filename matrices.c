#include <stdio.h>
#include <stdlib.h>

float determinant(float m[4]) { return (m[0] * m[3]) - (m[1] * m[2]); }

void scalarMultiply(float scalar, float m[4], float dest[4]) {
  for (int i = 0; i < 4; i++) {
    dest[i] = scalar * m[i];
  }
}

void adjugate(float m[4], float dest[4]) {
  dest[0] = m[3];
  dest[3] = m[0];
  dest[1] = -1 * m[1];
  dest[2] = -1 * m[2];
}

int inverse(float m[4], float dest[4]) {
  float adj[4] = {0, 0, 0, 0};
  adjugate(m, adj);
  float det = determinant(m);
  if (det == 0) {
    printf("This set of equations is impossible...\n");
    return 1;
  } else {
    scalarMultiply(1.0 / det, adj, dest);
    return 0;
  }
}

float dotProduct(float v1[2], float v2[2]) {
  return v1[0] * v2[0] + v1[1] * v2[1];
}

void multiplyMatrixWithVector(float m[4], float v[2], float dest[2]) {
  float row1[2] = {m[0], m[1]};
  float row2[2] = {m[2], m[3]};
  dest[0] = dotProduct(row1, v);
  dest[1] = dotProduct(row2, v);
}

int main(int argc, char *argv[]) {
  if (argc != 7 && argc != 9) {
    printf("# Simultaneous Equation Solver\n");
    printf("ax + by = c\n");
    printf("dx + ey = f\n");
    printf("Usage: %s <a> <b> <c> <d> <e> <f> [var1] [var2]\n", argv[0]);
    return 1;
  }

  // Setting all of the variables
  float x1 = atof(argv[1]);
  float y1 = atof(argv[2]);
  float res1 = atof(argv[3]);
  float x2 = atof(argv[4]);
  float y2 = atof(argv[5]);
  float res2 = atof(argv[6]);

  char *var1 = "x";
  char *var2 = "y";
  if (argc == 9) {
    var1 = argv[7];
    var2 = argv[8];
  }

  float A[4] = {x1, y1, x2, y2};
  float b[2] = {res1, res2};

  printf("We will solve these two equations: \n");
  printf("%.1f%s + %.1f%s = %.1f\n", x1, var1, y1, var2, res1);
  printf("%.1f%s + %.1f%s = %.1f\n", x2, var1, y2, var2, res2);
  printf("\n");

  float inv[4] = {};
  int err = inverse(A, inv);
  // if the determinant is zero
  if (err == 1) {
    return 1;
  }

  float answer[2] = {};
  multiplyMatrixWithVector(inv, b, answer);
  printf("%s = %.3f & %s = %.3f\n", var1, answer[0], var2, answer[1]);

  return 0;
}
