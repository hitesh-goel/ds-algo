package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

// Complete the connectedCities function below.
func connectedCities(n int32, g int32, originCities []int32, destinationCities []int32) []int32 {
	arr := make(map[int32][]int32)
	res := []int32{}

	//Calucate divisors of city
	for i := range originCities {
		if _, ok := arr[originCities[i]]; !ok {
			arr[originCities[i]] = ds(originCities[i], g)
		}
	}
	for i := range destinationCities {
		if _, ok := arr[destinationCities[i]]; !ok {
			arr[destinationCities[i]] = ds(destinationCities[i], g)
		}
	}

	for i := range originCities {
		route := false
		for j := range destinationCities {
			if len(int2Arrays(arr[originCities[i]], arr[destinationCities[j]], g)) > 0 && !route {
				res = append(res, 1)
				route = true
			}
		}
		if !route {
			res = append(res, 0)
		}
	}
	return res
}

func int2Arrays(a, b []int32, q int32) []int32 {
	h, l := a, b
	if len(b) > len(a) {
		h, l = b, a
	}
	ints := []int32{}
	for _, x := range h {
		for _, y := range l {
			if x == y && x > q {
				ints = append(ints, x)
			}
		}
	}
	return ints
}

func ds(a, g int32) []int32 {
	arr := []int32{}
	for i := g + 1; i <= a; i++ {
		if a%i == 0 {
			arr = append(arr, i)
		}
	}
	return arr
}

func min(a, b int32) int32 {
	if a < b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout := os.Stdout

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	gTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	g := int32(gTemp)

	originCitiesCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var originCities []int32

	for i := 0; i < int(originCitiesCount); i++ {
		originCitiesItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		originCitiesItem := int32(originCitiesItemTemp)
		originCities = append(originCities, originCitiesItem)
	}

	destinationCitiesCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var destinationCities []int32

	for i := 0; i < int(destinationCitiesCount); i++ {
		destinationCitiesItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		destinationCitiesItem := int32(destinationCitiesItemTemp)
		destinationCities = append(destinationCities, destinationCitiesItem)
	}

	res := connectedCities(n, g, originCities, destinationCities)

	log.Println(res)

	for i, resItem := range res {
		fmt.Fprintf(writer, "%d", resItem)

		if i != len(res)-1 {
			fmt.Fprintf(writer, "\n")
		}
	}

	fmt.Fprintf(writer, "\n")

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

/*
Sample Case 0
	Input
	6
	0
	4
	1
	4
	3
	6
	4
	3
	6
	2
	5

	Output
	1
	1
	1
	1
*/

/*
Sample Case 1
	Input
	6
	1
	4
	1 (1)       , 3 (1,3)
	2 (1,2)     , 3 (1,3)
	4 (1,2,4)   , 3 (1,3)
	6 (1,2,3,6) , 4 (1,2,4)

	Output
	0
	1
	1
	1
*/

/*
Sample Case 2
	Input
	10
	1
	4
	10 (1,2,5,10) , 3 (1,3)
	4  (1,2,4)    , 6 (1,2,3,6)
	3  (1,3)      , 2 (1,2)
	6  (1,2,3,6)  , 9 (1,3,9)

	Output
	1
	1
	1
	1
*/
