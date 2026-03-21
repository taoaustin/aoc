package day9

import (
	"strconv"
	"strings"

	"aoc2025/util"
)

type Coord struct {
	Col int
	Row int
}

func abs(i int) int {
	if i >= 0 {
		return i
	}
	return -i
}

func Solve() (int, int, error) {
	lines := util.ReadFileLines(9, false)
	var coords []Coord
	for _, line := range lines {
		parts := strings.Split(line, ",")
		col, err := strconv.ParseInt(parts[0], 10, 64)
		if err != nil {
			return 0, 0, err
		}
		row, err := strconv.ParseInt(parts[1], 10, 64)
		if err != nil {
			return 0, 0, err
		}
		coords = append(coords, Coord{Row: int(row), Col: int(col)})
	}
	p1, err := p1(coords)
	if err != nil {
		return 0, 0, err
	}
	p2, err := p2(coords)
	if err != nil {
		return 0, 0, err
	}

	return p1, p2, nil
}

func p1(corners []Coord) (int, error) {
	maxArea := 0
	for _, corner1 := range corners {
		for _, corner2 := range corners {
			w := abs(corner1.Col-corner2.Col) + 1
			l := abs(corner1.Row-corner2.Row) + 1
			if w*l > maxArea {
				maxArea = w * l
			}

		}
	}
	return maxArea, nil
}

func p2(coords []Coord) (int, error) {
	edges := getEdges(coords)
	maxArea := 0
	for _, corner1 := range coords {
		for _, corner2 := range coords {

			w := abs(corner1.Col-corner2.Col) + 1
			l := abs(corner1.Row-corner2.Row) + 1
			// if area is less than max
			if w*l <= maxArea {
				continue
			}

			allCorners := []Coord{
				{
					Row: corner1.Row,
					Col: corner2.Col,
				},
				{
					Row: corner2.Row,
					Col: corner1.Col,
				},
				{
					Row: corner1.Row,
					Col: corner1.Col,
				},
				{
					Row: corner2.Row,
					Col: corner2.Col,
				},
			}
			// if all corners are within the polygon
			f := true
			for _, corner := range allCorners {
				if !inPolygon(corner, edges) {
					f = false
				}
			}
			if !f {
				continue
			}
			// if no edges cross into outside the polygon
			if ok := crossingEdges(
				min(corner1.Col, corner2.Col),
				max(corner1.Col, corner2.Col),
				min(corner1.Row, corner2.Row),
				max(corner1.Row, corner2.Row),
				edges,
			); ok {
				continue
			}
			maxArea = w * l
		}
	}
	return maxArea, nil
}

func getEdges(coords []Coord) map[Coord]struct{} {
	edge := make(map[Coord]struct{})
	first := coords[0]
	prev := first
	for _, coord := range append(coords[1:], first) {
		if prev.Row != coord.Row {
			for diffRow := range abs(coord.Row-prev.Row) + 1 {
				edge[Coord{
					Row: min(coord.Row, prev.Row) + diffRow,
					Col: coord.Col,
				}] = struct{}{}
			}
		} else {
			for diffCol := range abs(coord.Col-prev.Col) + 1 {
				edge[Coord{
					Row: coord.Row,
					Col: min(coord.Col, prev.Col) + diffCol,
				}] = struct{}{}
			}
		}
		prev = coord
	}
	return edge
}

func crossingEdges(minCol, maxCol, minRow, maxRow int, edges map[Coord]struct{}) bool {
	i := minRow + 1
	for i < maxRow {
		_, ok0 := edges[Coord{Col: minCol, Row: i}]
		_, ok1 := edges[Coord{minCol + 1, i}]
		_, ok2 := edges[Coord{minCol - 1, i}]
		if ok0 && ok1 && ok2 {
			return true
		}
		_, ok0 = edges[Coord{Col: maxCol, Row: i}]
		_, ok1 = edges[Coord{Col: maxCol + 1, Row: i}]
		_, ok2 = edges[Coord{Col: maxCol - 1, Row: i}]
		if ok0 && ok1 && ok2 {
			return true
		}
		i++
	}
	i = minCol + 1
	for i < maxCol {
		_, ok0 := edges[Coord{Col: i, Row: minRow}]
		_, ok1 := edges[Coord{Col: i, Row: minRow + 1}]
		_, ok2 := edges[Coord{Col: i, Row: minRow - 1}]
		if ok0 && ok1 && ok2 {
			return true
		}
		_, ok0 = edges[Coord{Col: i, Row: maxRow}]
		_, ok1 = edges[Coord{Col: i, Row: maxRow + 1}]
		_, ok2 = edges[Coord{Col: i, Row: maxRow - 1}]
		if ok0 && ok1 && ok2 {
			return true
		}
		i++
	}
	return false
}

var memo = make(map[Coord]bool)

func inPolygon(coord Coord, edges map[Coord]struct{}) bool {
	if _, ok := edges[coord]; ok {
		memo[coord] = true
		return true
	} else if res, ok := memo[coord]; ok {
		return res
	}
	crosses := 0
	row := coord.Row
	col := coord.Col
	for coord.Row > 0 && coord.Col > 0 {
		coord.Row--
		coord.Col--
		_, ok := edges[coord]
		if !ok {
			continue
		}
		above := 0
		_, ok = edges[Coord{Col: coord.Col, Row: coord.Row - 1}]
		if ok {
			above++
		}
		_, ok = edges[Coord{Col: coord.Col + 1, Row: coord.Row}]
		if ok {
			above++
		}
		if above == 1 {
			crosses++
		}
	}
	memo[Coord{Row: row, Col: col}] = crosses%2 == 1
	return crosses%2 == 1
}
