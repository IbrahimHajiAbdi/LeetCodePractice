package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(numDecodings("11106"))
}

func numDecodings(s string) int {
	seen := map[int]int{}
	var dp func(int) int
	dp = func(i int) int {
		fmt.Println(i)
		if i >= len(s) {
			return 1
		}
		if string(s[i]) == "0" {
			return 0
		}
		if val, ok := seen[i]; ok {
			return val
		}

		if i < len(s)-1 {
			if num, _ := strconv.Atoi(s[i : i+2]); num <= 26 {
				seen[i] = dp(i+1) + dp(i+2)
				return seen[i]
			}
		}
		seen[i] = dp(i + 1)
		return seen[i]
	}
	return dp(0)
}
