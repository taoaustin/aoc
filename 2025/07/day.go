package day7

import (
	"aoc2025/util"
)

func Solve() (int, int, error) {
	grid, _, _ := util.ReadFileGrid(7, false)
	p1 := 0
	p2 := 0
	for col, ch := range grid[0] {
		if ch == 'S' {
			p1 = p1Solve(grid, 1, col)
			p2 = p2Solve(grid, 1, col)
		}
	}
	return p1, p2, nil
}

type Pair struct {
	A int
	B int
}

func p1Solve(grid [][]rune, row int, col int) int {
	memo := make(map[Pair]struct{})
	memo[Pair{A: 0, B: 0}] = struct{}{}
	var numSplits func(grid [][]rune, row int, col int) int
	numSplits = func(grid [][]rune, row int, col int) int {
		_, visited := memo[Pair{A: row, B: col}]
		memo[Pair{row, col}] = struct{}{}
		if row == len(grid) {
			return 0
		}

		if grid[row][col] == '.' {
			if !visited {
				return numSplits(grid, row+1, col)
			} else {
				return 0
			}
		}

		if grid[row][col] == '^' {
			if !visited {
				return 1 + numSplits(grid, row+1, col-1) + numSplits(grid, row+1, col+1)
			} else {
				return numSplits(grid, row+1, col-1) + numSplits(grid, row+1, col+1)
			}
		}
		return 0
	}
	return numSplits(grid, row, col)
}

func p2Solve(grid [][]rune, row int, col int) int {
	memo := make(map[Pair]int)

	var uniqPaths func(grid [][]rune, row int, col int) int
	uniqPaths = func(grid [][]rune, row int, col int) int {
		res, visited := memo[Pair{A: row, B: col}]
		if visited {
			return res
		}
		if row == len(grid) {
			return 1
		}

		if grid[row][col] == '.' {
			return uniqPaths(grid, row+1, col)
		}

		if grid[row][col] == '^' {
			res = uniqPaths(grid, row+1, col-1) + uniqPaths(grid, row+1, col+1)
			memo[Pair{row, col}] = res
			return res
		}
		return 0
	}
	return uniqPaths(grid, row, col)
}
