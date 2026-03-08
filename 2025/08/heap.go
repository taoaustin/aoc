package day8

type Pair struct {
	A Pos
	B Pos
}

type PosPairHeap struct {
	l []Pair
}

func (h PosPairHeap) Len() int {
	return len(h.l)
}

func (h PosPairHeap) Less(i, j int) bool {
	return h.l[i].A.Dist(h.l[i].B) < h.l[j].A.Dist(h.l[j].B)
}

func (h PosPairHeap) Swap(i, j int) {
	tmp := h.l[i]
	h.l[i] = h.l[j]
	h.l[j] = tmp
}

func (h *PosPairHeap) Push(x any) {
	h.l = append(h.l, x.(Pair))
}

func (h *PosPairHeap) Pop() any {
	res := h.l[len(h.l)-1]
	h.l = h.l[0 : len(h.l)-1]
	return res
}
