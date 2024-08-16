package main

import "fmt"

type TrieNode struct {
	Children map[string]*TrieNode
	Terminal bool
}

type WordDictionary struct {
	Root *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{
		Root: &TrieNode{
			Children: make(map[string]*TrieNode),
			Terminal: false,
		},
	}
}

func (this *WordDictionary) AddWord(word string) {
	ptr := this.Root

	for _, char := range word {
		if _, ok := ptr.Children[string(char)]; !ok {
			ptr.Children[string(char)] = &TrieNode{
				Children: map[string]*TrieNode{},
				Terminal: false,
			}
		}
		ptr = ptr.Children[string(char)]
	}

	ptr.Terminal = true
}

func (this *WordDictionary) Search(word string) bool {
	if word == "" {
		return false
	}
	return this.SearchRecursive(word, 0, this.Root)
}

func (this *WordDictionary) SearchRecursive(word string, index int, currNode *TrieNode) bool {
	if index == len(word) {
		if currNode.Terminal {
			return true
		} else {
			return false
		}
	}
	if string(word[index]) == "." {
		for _, val := range currNode.Children {
			if this.SearchRecursive(word, index+1, val) {
				return true
			}
		}
	}
	if _, ok := currNode.Children[string(word[index])]; !ok {
		return false
	}
	return this.SearchRecursive(word, index+1, currNode.Children[string(word[index])])
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */

func main() {
	obj := Constructor()
	obj.AddWord("bad")
	param_2 := obj.Search("bad")
	fmt.Println([]bool{
		param_2,
	})
}
