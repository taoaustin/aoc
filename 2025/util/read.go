package util

import (
	"bufio"
	"fmt"
	"os"
)

func ReadFileString(day int, test bool) string {
	b, err := os.ReadFile(getInputPath(day, test))
	if err != nil {
		panic(err)
	}
	return string(b)
}

func ReadFileLines(day int, test bool) []string {
	file, err := os.Open(getInputPath(day, test))
	if err != nil {
		panic(err)
	}
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func getInputPath(day int, test bool) string {
	fileName := "input"
	if test {
		fileName += "_test"
	}
	fileName += ".txt"
	return fmt.Sprintf("%02d/%s", day, fileName)
}
