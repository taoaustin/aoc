package day10

import (
	"aoc2025/util"
	"fmt"
	"strconv"
	"strings"
)

func Solve() (int, int, error) {
	lines := util.ReadFileLines(10, true)
	p1 := 0
	p2 := 0
	for _, line := range lines {
		state, buttons, _ := parseLine(line)
		p1 += int(minSteps(state, buttons))
		// p2 += minJolt(joltage, buttons)
	}
	return p1, p2, nil
}

func parseLine(line string) (state uint16, buttons []uint16, joltage []uint16) {
	parts := strings.Split(line[1:], "] ")
	for i, r := range parts[0] {
		if r == '#' {
			state += 1 << i
		}
	}
	parts = strings.Split(parts[1], " ")
	joltage = util.Map(strings.Split(parts[len(parts)-1][1:len(parts[len(parts)-1])-1], ","),
		func(j string) uint16 {
			res, err := strconv.ParseUint(j, 10, 16)
			if err != nil {
				fmt.Println(err)
				panic("unexpected parse")
			}
			return uint16(res)
		})
	for _, s := range parts[:len(parts)-1] {
		b := strings.Split(s[1:len(s)-1], ",")
		var mask uint16
		for _, n := range b {
			res, err := strconv.ParseInt(n, 10, 8)
			if err != nil {
				fmt.Println(err)
				panic("unexpected parse error")
			}
			mask += 1 << res
		}
		buttons = append(buttons, mask)
	}
	return
}

func minSteps(state uint16, buttons []uint16) uint8 {
	memo := make(map[uint16]uint8)
	memo[0] = 0
	q := []uint16{0}
	for len(q) > 0 {
		st := q[0]
		q = q[1:]
		if st == state {
			break
		}
		steps := memo[st]
		for _, mask := range buttons {
			nState := st ^ mask
			if _, ok := memo[nState]; !ok {
				memo[nState] = steps + 1
				q = append(q, nState)
			}
		}

	}
	return memo[state]
}

func minJolt(joltage []uint16, buttons []uint16) int {
	return 0
}
