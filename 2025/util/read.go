package util

import (
	"fmt"
	"os"
	"strings"
)

func ReadFileString(day int, test bool) string {
	b, err := os.ReadFile(getInputPath(day, test))
	if err != nil {
		panic(err)
	}
	return string(b)
}

func ReadFileLines(day int, test bool) []string {
	str := ReadFileString(day, test)
	lines := strings.Split(str, "\n")
	if len(lines[len(lines)-1]) == 0 {
		return lines[0 : len(lines)-1]
	}
	return lines
}

func ReadFileGrid(day int, test bool) (res [][]rune, width int, length int) {
	lines := ReadFileLines(day, test)
	for _, line := range lines {
		res = append(res, []rune(line))
	}
	width = len(res[0])
	for _, row := range res {
		if len(row) != width {
			panic(fmt.Sprintf("unexpected width: %d (expected %d)", len(row), width))
		}
	}
	length = len(res)
	return
}

func getInputPath(day int, test bool) string {
	fileName := "input"
	if test {
		fileName += "_test"
	}
	fileName += ".txt"
	return fmt.Sprintf("%02d/%s", day, fileName)
}
