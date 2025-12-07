package day2

import (
	"strconv"
	"strings"

	"aoc2025/util"
)

func Solve() (int64, int64) {
	file := util.ReadFileString(2, false)
	var p1 int64 = 0
	var p2 int64 = 0
	intervals := strings.SplitSeq(file, ",")
	for interval := range intervals {
		p1 += findInvalid(interval)
		p2 += findInvalidP2(interval)
	}

	return p1, p2
}

func findInvalid(interval string) int64 {
	var res int64 = 0
	parts := strings.Split(interval, "-")

	intervalMin, err := strconv.ParseInt(parts[0], 10, 64)
	if err != nil {
		panic(err)
	}
	intervalMax, err := strconv.ParseInt(strings.TrimSpace(parts[1]), 10, 64)
	if err != nil {
		panic(err)
	}
	doubleHalf := "1"
	invalidVal, err := strconv.ParseInt(doubleHalf+doubleHalf, 10, 64)
	if err != nil {
		panic(err)
	}
	for invalidVal <= intervalMax {
		if invalidVal >= intervalMin {
			res += invalidVal
		}
		tmp, err := strconv.ParseInt(doubleHalf, 10, 64)
		if err != nil {
			panic(err)
		}
		doubleHalf = strconv.FormatInt(tmp+1, 10)
		invalidVal, err = strconv.ParseInt(doubleHalf+doubleHalf, 10, 64)
		if err != nil {
			panic(err)
		}
	}
	return res
}

func findInvalidP2(interval string) int64 {
	var res int64 = 0
	parts := strings.Split(interval, "-")

	intervalMin, err := strconv.ParseInt(parts[0], 10, 64)
	if err != nil {
		panic(err)
	}
	intervalMax, err := strconv.ParseInt(strings.TrimSpace(parts[1]), 10, 64)
	if err != nil {
		panic(err)
	}
	for i := intervalMin; i <= intervalMax; i++ {
		iStr := strconv.FormatInt(i, 10)
		rpt := strings.Index((iStr + iStr)[1:], iStr)
		if rpt != len(iStr)-1 {
			res += i
		}
	}
	return res
}
