package main

import (
	"fmt"
	"math"
	"strconv"
)

var digitToLetters = map[rune]string{
	'0': "ZERO",
	'1': "ONE",
	'2': "TWO",
	'3': "THREE",
	'4': "FOUR",
	'5': "FIVE",
	'6': "SIX",
	'7': "SEVEN",
	'8': "EIGHT",
	'9': "NINE",
}

var allNumsAsLetters = getAllNumsAsLetters()

func numToLetters(num string) string {
	result := ""
	for _, digit := range num {
		result += digitToLetters[digit]
	}
	return result
}

func getAllNumsAsLetters() []string {
	results := []string{}
	for i := 1; i < 1000; i++ {
		results = append(results, numToLetters(strconv.Itoa(i)))
	}
	return results
}

func canBeTransformed(num1, num2 string) bool {
	num1map := map[rune]int{}
	for _, digit := range num1 {
		num1map[digit] += 1
	}

	num2map := map[rune]int{}
	for _, digit := range num2 {
		num2map[digit] += 1
	}

	letters := map[rune]interface{}{}
	for digit, _ := range num1map {
		letters[digit] = 0
	}
	for digit, _ := range num2map {
		letters[digit] = 0
	}

	differences := 0
	for letter, _ := range letters {
		num1val, letterIn1 := num1map[letter]
		num2val, letterIn2 := num2map[letter]
		if letterIn1 && letterIn2 {
			differences += int(math.Abs(float64(num1val) - float64(num2val)))
		} else if letterIn1 {
			differences += num1val
		} else {
			differences += num2val
		}
	}

	return differences <= 5
}

func getDirectTransformations(num string) []string {
	results := []string{}
	for _, newNum := range allNumsAsLetters {
		if canBeTransformed(num, newNum) {
			results = append(results, newNum)
		}
	}
	return results
}

func findNumberLadderSize(num1, num2 string, masterMap map[string][]string) int {
	numsToCheck := map[string]interface{}{num1: 0}
	alreadySeen := map[string]interface{}{}
	i := 0

	for true {
		newNumsToCheck := map[string]interface{}{}
		for num := range numsToCheck {
			if _, ok := alreadySeen[num]; ok {
				continue
			}
			if num == num2 {
				return i
			}

			alreadySeen[num] = 0
			for _, n := range masterMap[num] {
				if _, ok := alreadySeen[n]; !ok {
					newNumsToCheck[n] = 0
				}
			}
		}

		numsToCheck = newNumsToCheck
		i++
	}
	return -1
}

func main() {
	inputs := [3][2]string{}

	for i := range 3 {
		var j, k string
		fmt.Scanf("%v %v", &j, &k)
		inputs[i][0] = numToLetters(j)
		inputs[i][1] = numToLetters(k)
	}

	masterMap := map[string][]string{}
	for _, num := range allNumsAsLetters {
		masterMap[num] = getDirectTransformations(num)
	}

	for _, input := range inputs {
		fmt.Println(findNumberLadderSize(input[0], input[1], masterMap))
	}
}
