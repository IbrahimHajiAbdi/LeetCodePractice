package main

import "fmt"

type Coords struct {
	y int
	x int
}

func numIslands(grid [][]byte) int {
	seen := map[Coords]struct{}{}

	dfs := func() {

	}
}

func main() {
	fmt.Println(numIslands())
}
