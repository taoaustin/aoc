package day5

import (
	"fmt"
	"slices"
	"strconv"
	"strings"

	"aoc2025/util"
)

func Solve() (int64, int64, error) {
	lines := util.ReadFileLines(5, false)

	var ranges [][2]int64
	var err error
	var i int
	var line string
	for i, line = range lines {
		if line == "" {
			break
		}
	}
	ranges, err = parseRanges(lines[:i])
	if err != nil {
		return 0, 0, err
	}
	ids := util.Map(lines[i+1:], func(s string) int64 {
		i, _ := strconv.ParseInt(s, 10, 64)
		return i
	})

	slices.SortFunc(ranges, func(a [2]int64, b [2]int64) int {
		return int(a[0] - b[0])
	})
	ranges = mergeRanges(ranges)
	silver := countValidIDs(ranges, ids)
	gold := allValidIDs(ranges)
	return silver, gold, nil
}

func parseRanges(intervals []string) ([][2]int64, error) {
	var res [][2]int64
	for _, interval := range intervals {
		parts := strings.Split(interval, "-")
		if len(parts) != 2 {
			return nil, fmt.Errorf("expected interval size")
		}
		num1, err := strconv.ParseInt(parts[0], 10, 64)
		if err != nil {
			return nil, err
		}
		num2, err := strconv.ParseInt(parts[1], 10, 64)
		if err != nil {
			return nil, err
		}
		res = append(res, [2]int64{num1, num2})
	}
	return res, nil
}

func mergeRanges(ranges [][2]int64) [][2]int64 {
	var res [][2]int64
	for _, r := range ranges {
		if len(res) == 0 {
			res = append(res, r)
			continue
		}
		if r[0] <= res[len(res)-1][1] {
			res[len(res)-1][1] = max(r[1], res[len(res)-1][1])
		} else {
			res = append(res, r)
		}
	}
	return res
}

func countValidIDs(ranges [][2]int64, ids []int64) int64 {
	var count int64 = 0
	for _, id := range ids {
		if idInSomeRange(id, ranges) {
			count++
		}
	}
	return count
}

func idInSomeRange(id int64, ranges [][2]int64) bool {
	for _, r := range ranges {
		if id >= r[0] && id <= r[1] {
			return true
		}
	}
	return false
}

func allValidIDs(ranges [][2]int64) int64 {
	var valids int64 = 0
	for _, r := range ranges {
		valids += (r[1] - r[0] + 1)
	}
	return valids
}
