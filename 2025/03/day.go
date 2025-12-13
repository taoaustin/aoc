package day3

import (
	"math"

	"aoc2025/util"
)

func Solve() (int64, int64) {
	lines := util.ReadFileLines(3, false)
	intLines := util.Map(lines, func(item string) []int64 {
		res := make([]int64, len(item))
		for i, s := range item {
			res[i] = util.Atoi(string(s))
		}
		return res
	})
	var p1 int64 = 0
	var p2 int64 = 0
	for _, line := range intLines {
		p1 += findMax(line, 2)
		p2 += findMax(line, 12)
	}
	return p1, p2
}

func findMax(line []int64, digits int) int64 {
	var res int64 = 0
	nextStart := 0
	for _i := range digits {
		i := digits - _i - 1
		curMax := line[nextStart]
		curMaxIdx := 0
		for j, jolt := range line[nextStart : len(line)-i] {
			if jolt > curMax {
				curMax = jolt
				curMaxIdx = j
			}
		}
		res += (curMax * powInt(10, i))
		nextStart += curMaxIdx + 1
	}
	return res
}

func powInt(x, y int) int64 {
	return int64(math.Pow(float64(x), float64(y)))
}
