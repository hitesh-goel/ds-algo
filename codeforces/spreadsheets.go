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
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	t, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)

	writer := bufio.NewWriterSize(os.Stdout, 1024*1024)

	for i := int64(0); i < t; i++ {
		s := readLine(reader)
		fmt.Fprintf(writer, "%s\n", writeAnotherNumeric(s))
	}

	writer.Flush()
}

func writeAnotherNumeric(s string) string {
	if isRowColumn(s) {
		return convertToSpreadsheetFormat(s)
	}
	return convertToRowColumn(s)
}

func convertToRowColumn(s string) string {
	return ""
}

func convertToSpreadsheetFormat(s string) string {
	return ""
}

func isRowColumn(s string) bool {
	if len(s) < 4 {
		return false
	}
	if 65 <= s[0] && s[0] <= 90 && 65 <= s[1] && s[1] <= 90 {
		return false
	}
	return true
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
