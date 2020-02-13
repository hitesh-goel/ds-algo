package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	s := readLine(reader)

	minLengthTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	minLength := int32(minLengthTemp)

	maxLengthTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	maxLength := int32(maxLengthTemp)

	maxUniqueTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	maxUnique := int32(maxUniqueTemp)

	res := getMaxOccurrences(s, minLength, maxLength, maxUnique)

	fmt.Fprintf(writer, "%d\n", res)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

// Complete the getMaxOccurrences function below.
func getMaxOccurrences(s string, minLength int32, maxLength int32, maxUnique int32) int32 {
	//Divide the problem
	// 1. Get all possible Sub Strings with minLength & maxLength
	// 2. Get only SubStrings whose value is less than or ex to maxUnique
	// 3. Calcaulate occurences of each substring
	// return max no Occurences of a SubString.
	for i := minLength; i <= maxLength; i++ {

	}
}
