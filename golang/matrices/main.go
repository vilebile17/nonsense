package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
)

type (
	Vector []float64
	Matrix []Vector
)

func (m Matrix) Print() {
	fmt.Println()
	for _, line := range m {
		fmt.Println(line)
	}
	fmt.Println()
}

func (v Vector) Print() {
	fmt.Println()
	fmt.Println(v)
	fmt.Println()
}

func (v Vector) ToMatrix() Matrix {
	m := Matrix{}
	for i := range v {
		m = append(m, Vector{v[i]})
	}
	return m
}

// isAdditionValid: A helper function for both add() and subtract()
func isAdditionValid(m1, m2 Matrix) bool {
	if len(m1) != len(m2) {
		return false
	}
	for i := range m1 {
		if len(m1[i]) != len(m2[i]) {
			return false
		}
	}
	return true
}

func Add(m1, m2 Matrix) (Matrix, error) {
	if !isAdditionValid(m1, m2) {
		return Matrix{}, fmt.Errorf("both matrices need to be the same size: %dx%d * %dx%d", len(m1), len(m1[0]), len(m2), len(m2[0]))
	}

	newM := Matrix{}
	for i := range m1 {
		newM = append(newM, Vector{})
		for j := range m1[i] {
			newM[i] = append(newM[i], m1[i][j]+m2[i][j])
		}
	}
	return newM, nil
}

func Subtract(m1, m2 Matrix) (Matrix, error) {
	if !isAdditionValid(m1, m2) {
		return Matrix{}, fmt.Errorf("both matrices need to be the same size: %dx%d * %dx%d", len(m1), len(m1[0]), len(m2), len(m2[0]))
	}

	newM := Matrix{}
	for i := range m1 {
		newM = append(newM, Vector{})
		for j := range m1[i] {
			newM[i] = append(newM[i], m1[i][j]-m2[i][j])
		}
	}
	return newM, nil
}

func ScalarMultiply(s float64, m Matrix) Matrix {
	newM := Matrix{}
	for i := range m {
		newM = append(newM, Vector{})
		for j := range m[i] {
			newM[i] = append(newM[i], m[i][j]*s)
		}
	}
	return newM
}

// dotProduct: A helper function for multiply()
func DotProduct(v1, v2 Vector) (float64, error) {
	if len(v1) != len(v2) {
		return 0.0, errors.New("the two vectors must be the same size")
	}
	sumSoFar := 0.0
	for i := range v1 {
		sumSoFar += v1[i] * v2[i]
	}
	return sumSoFar, nil
}

// getColumn: A helper function for multiply()
func (m Matrix) getColumn(n int) Vector {
	newV := Vector{}
	for _, row := range m {
		newV = append(newV, row[n])
	}
	return newV
}

func Multiply(m1, m2 Matrix) (Matrix, error) {
	if len(m1[0]) != len(m2) {
		return Matrix{}, fmt.Errorf("matrix multiplication isn't possible here: %dx%d * %dx%d", len(m1), len(m1[0]), len(m2), len(m2[0]))
	}

	newM := Matrix{}
	for i, row := range m1 {
		newM = append(newM, Vector{})
		for j := range len(m2[0]) {
			column := m2.getColumn(j)
			dp, err := DotProduct(row, column)
			if err != nil {
				return Matrix{}, err
			}
			newM[i] = append(newM[i], dp)
		}
	}
	return newM, nil
}

func (m Matrix) GetDeterminant() (float64, error) {
	if len(m) != 2 || len(m[0]) != 2 {
		return 0.0, errors.New("sorry, I can only find the determinant of 2x2 matrices")
	}
	return m[0][0]*m[1][1] - m[1][0]*m[0][1], nil
}

func (m Matrix) GetAdjugate() (Matrix, error) {
	if len(m) != 2 || len(m[0]) != 2 {
		return Matrix{}, errors.New("sorry, I can only find the adjugate of 2x2 matrices")
	}

	newM := Matrix{}
	newM = append(newM, Vector{m[1][1], -1 * m[0][1]})
	newM = append(newM, Vector{-1 * m[1][0], m[0][0]})
	return newM, nil
}

func (m Matrix) GetInverse() (Matrix, error) {
	adj, err := m.GetAdjugate()
	if err != nil {
		return Matrix{}, err
	}
	det, err := m.GetDeterminant()
	if err != nil {
		return Matrix{}, err
	}
	return GetInverse(det, adj)
}

func GetInverse(det float64, adj Matrix) (Matrix, error) {
	if det == 0 {
		return Matrix{}, errors.New("determinant is zero")
	}
	return ScalarMultiply(1/det, adj), nil
}

func main() {
	if len(os.Args) != 7 {
		log.Fatal("must have 6 arguments (Ax + By = C, Dx + Ey = F)")
	}
	var x1, y1, res1, x2, y2, res2 float64
	vals := []*float64{&x1, &y1, &res1, &x2, &y2, &res2}
	for i := range 6 {
		val, err := strconv.ParseFloat(os.Args[i+1], 64)
		if err != nil {
			log.Fatal(err)
		}
		*vals[i] = val
	}

	fmt.Println("We will solve the following equations using matrices:")
	fmt.Printf("%vx + %vy = %v\n", x1, y1, res1)
	fmt.Printf("%vx + %vy = %v\n", x2, y2, res2)
	fmt.Println()
	A := Matrix{
		{x1, y1},
		{x2, y2},
	}
	fmt.Println("A = ")
	A.Print()
	b := Vector{res1, res2}
	fmt.Println("b = ")
	b.Print()
	fmt.Println("X = ")
	fmt.Println()
	fmt.Println("[x, y]")
	fmt.Println()

	fmt.Println("AX = b")
	fmt.Println("A^-1 * AX = A^-1 * b")
	fmt.Println("IX = A^-1 * b")
	fmt.Println("X = A^-1 * b")

	inverseOfA, err := A.GetInverse()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("A^-1 = ")
	inverseOfA.Print()

	x, err := Multiply(inverseOfA, b.ToMatrix())
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("The matrix of unknowns (x, y) = A^-1 * b = ")
	x.Print()
}
