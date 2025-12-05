package day1

import (
	"fmt"
	"strconv"

	"aoc2025/util"
)

type Dir rune

const (
	DirL Dir = 'L'
	DirR Dir = 'R'
)

func Solve() (int, int) {
	lines := util.ReadFileLines(1, false)
	p1, p2 := MoveTheNeedle(lines)
	return p1, p2
}

func MoveTheNeedle(lines []string) (int, int) {
	password1 := 0
	password2 := 0
	needle := 50
	for _, line := range lines {
		oldNeedle := needle
		amt, err := strconv.ParseInt(line[1:], 10, 64)
		if err != nil {
			panic(err)
		}
		if line[0] == byte(DirL) {
			needle -= int(amt)
		} else if line[0] == byte(DirR) {
			needle += int(amt)
		} else {
			panic(fmt.Sprintf("unknown dir %c", line[0]))
		}
		if needle >= 100 {
			password2 += (needle / 100)
		} else if needle < 0 && oldNeedle == 0 {
			password2 += (needle / -100)
		} else if needle < 0 && oldNeedle != 0 {
			password2 += ((needle / -100) + 1)
		} else if needle == 0 {
			password2 += 1
		}

		needle = (needle%100 + 100) % 100
		if needle == 0 {
			password1++
		}
	}
	return password1, password2
}
