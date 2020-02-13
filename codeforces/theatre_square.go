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

	nTemp := strings.Split(readLine(reader), " ")

	t, err := strconv.ParseInt(nTemp[0], 10, 64)
	checkError(err)
	n := int32(t)

	t, err = strconv.ParseInt(nTemp[1], 10, 64)
	checkError(err)
	m := int32(t)

	t, err = strconv.ParseInt(nTemp[2], 10, 64)
	checkError(err)
	a := int32(t)

	writer := bufio.NewWriterSize(os.Stdout, 1024*1024)
	fmt.Fprintf(writer, "%d\n", minSquares(n, m, a))

	writer.Flush()
}

func minSquares(n, m, a int32) int32 {
	var l, b int32
	l = n / a
	if n%a > 0 {
		l++
	}
	b = m / a
	if m%a > 0 {
		b++
	}
	return l * b
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
