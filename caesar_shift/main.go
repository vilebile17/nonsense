package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func caesarShift(text string, shift int) string {
	const lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
	const upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	trueShift := shift % 26
	for trueShift < 0 {
		trueShift += 26
	}

	cipherText := ""
	for _, char := range text {
		if i := strings.IndexRune(lowerCaseLetters, char); i != -1 {
			cipherText += string(lowerCaseLetters[(i+trueShift)%26])
		} else if i := strings.IndexRune(upperCaseLetters, char); i != -1 {
			cipherText += string(upperCaseLetters[(i+trueShift)%26])
		} else {
			cipherText += string(char)
		}
	}

	return cipherText
}

func encrypt(text string, shift int) {
	fmt.Println(caesarShift(text, shift))
}

func decrypt(text string, shift int) {
	fmt.Println(caesarShift(text, -shift))
}

func bruteForce(text string) {
	for i := 25; i > 0; i-- {
		fmt.Printf("%s - Original shift %d\n", caesarShift(text, i), 26-i)
	}
}

func help() {
	fmt.Println("USAGE: caesarShift <command>")
	fmt.Println()
	fmt.Println("## Commands")
	fmt.Println("encrypt <plainText> <shift> - Encrypts the plain text and prints the cipher text. <shift> must be an integer")
	fmt.Println("decrypt <cipherText> <shift> - Decrypts the cipher text given that the original plain text was shifted over <shift> spaces. Again, <shift> must be an integer")
	fmt.Println("bruteForce <cipherText> - Prints all of the possible shifts for a cipher text")
	fmt.Println()
	fmt.Println("Note, you may need to wrap your text in quotation marks if it is multiple words long")
	os.Exit(1)
}

func main() {
	if len(os.Args) < 3 || len(os.Args) > 4 {
		help()
	}

	command := os.Args[1]
	text := os.Args[2]

	switch command {
	case "encrypt":
		if len(os.Args) == 3 {
			help()
		}

		shift, err := strconv.Atoi(os.Args[3])
		if err != nil {
			fmt.Println("ERROR: <shift> parameter must be an Integer")
			fmt.Println("USAGE: caesarShift encrypt <plainText> <shift>")
			os.Exit(1)
		}
		encrypt(text, shift)
	case "decrypt":
		if len(os.Args) == 3 {
			help()
		}

		shift, err := strconv.Atoi(os.Args[3])
		if err != nil {
			fmt.Println("ERROR: <shift> parameter must be an Integer")
			fmt.Println("USAGE: caesarShift decrypt <cipherText> <shift>")
			os.Exit(1)
		}
		decrypt(text, shift)
	case "bruteForce":
		bruteForce(text)
	default:
		help()
	}
}
