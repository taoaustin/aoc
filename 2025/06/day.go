package day6

import (
	"strconv"
	"strings"

	"aoc2025/util"
)

func Solve() (int64, int64, error) {
	lines := util.ReadFileLines(6, false)
	p1 := solveP1(lines)
	p2 := solveP2(lines)
	return p1, p2, nil
}

func solveP1(lines []string) int64 {
	tmp := util.Map(lines, func(line string) []string {
		return strings.Fields(line)
	})
	operators := tmp[len(tmp)-1]
	tmp = tmp[0 : len(tmp)-1]
	p1Vals := util.Map(tmp, func(t []string) []int64 {
		return util.Map(t, func(u string) int64 {
			i, err := strconv.ParseInt(u, 10, 64)
			if err != nil {
				panic(err)
			}
			return i
		})
	})
	var res int64 = 0
	for c := range p1Vals[0] {
		res += calcCol(p1Vals, operators[c], c)
	}
	return res
}

func calcCol(grid [][]int64, operator string, col int) int64 {
	var res int64 = 0
	if operator == "*" {
		res = 1
	}
	for _, row := range grid {
		switch operator {
		case "+":
			res += row[col]
		case "*":
			res *= row[col]
		}
	}
	return res
}

func solveP2(lines []string) int64 {
	numLines := lines[0 : len(lines)-1]
	opLine := lines[len(lines)-1]

	var res int64 = 0

	var curOp rune
	var partialRes int64 = 0

	i := 0
	for i < len(opLine) {
		if opLine[i] != ' ' {
			res += partialRes
		}
		switch opLine[i] {
		case '+':
			curOp = '+'
			partialRes = 0
		case '*':
			curOp = '*'
			partialRes = 1
		}

		s := ""
		for j := range len(numLines) {
			c := numLines[j][i]
			if c == ' ' {
				continue
			}
			s += string(c)
		}
		if s != "" {
			n, err := strconv.ParseInt(s, 10, 64)
			if err != nil {
				panic(err)
			}
			switch curOp {
			case '+':
				partialRes += n
			case '*':
				partialRes *= n
			}
		}
		i++
	}
	res += partialRes
	return res
}
