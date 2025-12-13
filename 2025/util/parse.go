package util

import "strconv"

func Atoi(s string) int64 {
	i, err := strconv.ParseInt(s, 10, 64)
	if err != nil {
		panic(err)
	}
	return i
}

func Map[T any, U any](s []T, fn func(T) U) []U {
	res := make([]U, len(s))
	for i, t := range s {
		res[i] = fn(t)
	}
	return res
}
