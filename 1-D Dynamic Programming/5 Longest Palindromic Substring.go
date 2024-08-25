package main

import "fmt"

type Coords struct {
	l int
	r int
}

func longestPalindrome(s string) string {
	seen := map[Coords]bool{}
	res := ""
	if len(s) == 1 {
		return string(s[0])
	}
	if len(s) == 2 {
		if s[0] == s[1] {
			return s
		}
		return string(s[0])
	}
	var validPalindrome func(int, int) bool
	var longest func(int, int, int)

	validPalindrome = func(l, r int) bool {
		for l < r {
			if s[l] == s[r] {
				l += 1
				r -= 1
			} else {
				return false
			}
		}
		return true
	}

	longest = func(l, r, currMax int) {
		coords := Coords{
			l: l,
			r: r,
		}
		if l == r || len(s[l:r+1]) < currMax {
			return
		}
		if _, ok := seen[coords]; ok {
			return
		}
		seen[coords] = validPalindrome(l, r)
		for k, v := range seen {
			if v && len(s[k.l:k.r+1]) > currMax {
				currMax = len(s[k.l : k.r+1])
			}
		}
		longest(l+1, r, currMax)
		longest(l, r-1, currMax)
	}
	longest(0, len(s)-1, 0)

	for coords, val := range seen {
		if val && (coords.r-coords.l) >= len(res) {
			res = s[coords.l : coords.r+1]
		}
	}
	fmt.Println("Length of seen:", len(seen))
	if res == "" {
		return string(s[0])
	}
	return res
}

func main() {
	fmt.Println(longestPalindrome("cbbd"))
	fmt.Println(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
}
