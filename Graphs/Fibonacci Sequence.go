package main

import "fmt"

func main() {
	// index : val
	seen := map[int]int{
		0: 0,
		1: 1,
	}
	var fib func(int) int
	fib = func(n int) int {
		if val, ok := seen[n]; ok {
			return val
		}
		seen[n] = fib(n-1) + fib(n-2)
		return seen[n]
	}
	fmt.Println(fib(-1))
}
