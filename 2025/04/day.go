package day4

import (
	"aoc2025/util"
)

func Solve() (int, int) {
	grid, width, length := util.ReadFileGrid(4, false)
	p1 := Check(grid, width, length)
	p2 := Check2(grid, width, length)
	return p1, p2
}

func Check(grid [][]rune, width int, length int) int {
	res := 0
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == '@' {
				adjacentRolls := 0
				for _, dir := range util.Adjacents {
					r, c := i+dir[0], j+dir[1]
					if r >= 0 && r < length && c >= 0 && c < width && grid[r][c] == '@' {
						adjacentRolls++
					}
				}
				if adjacentRolls < 4 {
					res++
				}
			}
		}
	}
	return res
}

// brutish, uncouth, primitive, prehistoric
func Check2(grid [][]rune, width int, length int) int {
	res := 0
	iter := 0
	for {
		for i := range grid {
			for j := range grid[i] {
				if grid[i][j] == '@' {
					adjacentRolls := 0
					for _, dir := range util.Adjacents {
						r, c := i+dir[0], j+dir[1]
						if r >= 0 && r < length && c >= 0 && c < width && grid[r][c] == '@' {
							adjacentRolls++
						}
					}
					if adjacentRolls < 4 {
						grid[i][j] = '.'
						iter++
					}
				}
			}
		}
		if iter == 0 {
			break
		} else {
			res += iter
			iter = 0
		}
	}
	return res
}
