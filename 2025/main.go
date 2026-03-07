package main

import (
	"fmt"
	"log"

	day7 "aoc2025/07"
)

func main() {
	// p1, p2 := day1.Solve()
	// p1, p2 := day2.Solve()
	// p1, p2 := day3.Solve()
	// p1, p2 := day4.Solve()
	// p1, p2, err := day5.Solve()
	// p1, p2, err := day6.Solve()
	p1, p2, err := day7.Solve()
	if err != nil {
		log.Fatalf("error: %v", err)
	}
	fmt.Println(p1, p2)
}
