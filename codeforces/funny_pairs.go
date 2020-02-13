package main

import (
	"bufio"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	writer := bufio.NewWriterSize(os.Stdout, 1024*1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	intArr := make([]int64, nTemp)

	arr := strings.Split(readLine(reader), " ")
	for _, v := range arr {
		b, err := strconv.ParseInt(v, 10, 64)
		if err != nil {
			log.Println(err)
		}
		intArr = append(intArr, b)
	}

	for i := int64(0); i < nTemp; i++ {
		for j := nTemp - 1; i >= 0; j-- {
			var l, r int64
			if intArr[i] > intArr[j] {
				r = intArr[i]
				l = intArr[j]
			} else {
				r = intArr[j]
				l = intArr[i]
			}
			if (r-l+1)%2 > 0 {
				isFunnyPair()
			}
		}
	}

	writer.Flush()
}

func isFunnyPair(arr []int64) bool {

}

func performXOROperations(arr []int64) int64 {
	var x int64
	if len(arr) > 2 {
		x = arr[0] ^ arr[1]
		for i := 2; i < len(arr); i++ {
			x ^= arr[i]
		}
	}
	return x
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
