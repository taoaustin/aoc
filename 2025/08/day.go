package day8

import (
	"container/heap"
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"

	"aoc2025/util"
)

func Solve() (int, int, error) {
	ppHeap1, numTotalPositions, err := initHeap()
	if err != nil {
		return 0, 0, err
	}
	ppHeap2 := &PosPairHeap{l: slices.Clone(ppHeap1.l)}

	circuits := createCircuits(ppHeap1, 1000)
	circuitsLens := util.Map(circuits, func(c map[Pos]struct{}) int {
		return len(c)
	})
	slices.Sort(circuitsLens)
	slices.Reverse(circuitsLens)
	p1 := circuitsLens[0] * circuitsLens[1] * circuitsLens[2]
	p2 := createMegaCircuit(ppHeap2, numTotalPositions)
	return p1, p2, nil
}

func initHeap() (*PosPairHeap, int, error) {
	var ppHeap []Pair
	lines := util.ReadFileLines(8, false)
	var l []Pos
	for _, line := range lines {
		parts := strings.Split(line, ",")
		if len(parts) != 3 {
			return nil, 0, fmt.Errorf("wrong num parts %d", len(parts))
		}
		x, err := strconv.ParseInt(parts[0], 10, 64)
		if err != nil {
			return nil, 0, err
		}
		y, err := strconv.ParseInt(parts[1], 10, 64)
		if err != nil {
			return nil, 0, err
		}
		z, err := strconv.ParseInt(parts[2], 10, 64)
		if err != nil {
			return nil, 0, err
		}
		l = append(l, Pos{X: int(x), Y: int(y), Z: int(z)})
	}

	for i := 0; i < len(l); i++ {
		for j := i + 1; j < len(l); j++ {
			ppHeap = append(ppHeap, Pair{l[i], l[j]})
		}
	}
	res := PosPairHeap{l: ppHeap}
	heap.Init(&res)
	return &res, len(l), nil
}

func createCircuits(ppHeap heap.Interface, steps int) []map[Pos]struct{} {
	var res []map[Pos]struct{}
	for range steps {
		pair := heap.Pop(ppHeap).(Pair)
		idxA := -1
		idxB := -1
		for i, m := range res {
			if _, ok := m[pair.A]; ok {
				idxA = i
			}
			if _, ok := m[pair.B]; ok {
				idxB = i
			}
		}
		if idxA == -1 && idxB == -1 {
			res = append(res, map[Pos]struct{}{pair.A: {}, pair.B: {}})
		} else if idxA == -1 && idxB != -1 {
			res[idxB][pair.A] = struct{}{}
		} else if idxA != -1 && idxB == -1 {
			res[idxA][pair.B] = struct{}{}
		} else if idxA != idxB {
			mA := res[idxA]
			mB := res[idxB]
			for k := range mB {
				mA[k] = struct{}{}
			}
			res[idxA] = mA
			res = append(res[0:idxB], res[idxB+1:]...)
		}
	}
	return res
}

func createMegaCircuit(ppHeap heap.Interface, numPositions int) int {
	var res []map[Pos]struct{}
	for {
		pair := heap.Pop(ppHeap).(Pair)
		idxA := -1
		idxB := -1
		for i, m := range res {
			if _, ok := m[pair.A]; ok {
				idxA = i
			}
			if _, ok := m[pair.B]; ok {
				idxB = i
			}
		}
		if idxA == -1 && idxB == -1 {
			res = append(res, map[Pos]struct{}{pair.A: {}, pair.B: {}})
		} else if idxA == -1 && idxB != -1 {
			res[idxB][pair.A] = struct{}{}
			if len(res[idxB]) == numPositions {
				return pair.A.X * pair.B.X
			}

		} else if idxA != -1 && idxB == -1 {
			res[idxA][pair.B] = struct{}{}
			if len(res[idxA]) == numPositions {
				return pair.A.X * pair.B.X
			}
		} else if idxA != idxB {
			mA := res[idxA]
			mB := res[idxB]
			for k := range mB {
				mA[k] = struct{}{}
			}
			res[idxA] = mA
			res = append(res[0:idxB], res[idxB+1:]...)
			if len(mA) == numPositions {
				return pair.A.X * pair.B.X
			}
		}
	}
}

type Pos struct {
	X int
	Y int
	Z int
}

func (p Pos) Dist(q Pos) float64 {
	return math.Sqrt(
		math.Pow((float64(p.X-q.X)), 2) +
			math.Pow((float64(p.Y-q.Y)), 2) +
			math.Pow((float64(p.Z-q.Z)), 2),
	)
}
