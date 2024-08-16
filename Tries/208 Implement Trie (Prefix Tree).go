package main

import "fmt"

type Trie struct {
	Children map[string]*Trie
	Terminal bool
}

func Constructor() Trie {
	return Trie{
		Children: map[string]*Trie{},
		Terminal: false,
	}
}

func (this *Trie) NewNode() *Trie {
	return &Trie{
		Children: make(map[string]*Trie),
		Terminal: false,
	}
}

func (this *Trie) Insert(word string) {
	if word == "" {
		return
	}
	if len(this.Children) == 0 {
		this.Children[string(word[0])] = this.NewNode()
	}
	ptr := this

	for i, char := range word {
		if _, ok := ptr.Children[string(char)]; !ok {
			ptr.Children[string(char)] = this.NewNode()
		}
		ptr = ptr.Children[string(char)]
		if i == len(word)-1 {
			ptr.Terminal = true
		}
	}

}

func (this *Trie) Search(word string) bool {
	ptr := this

	for i, char := range word {
		if _, ok := ptr.Children[string(char)]; !ok {
			return false
		}
		ptr = ptr.Children[string(char)]
		if i == len(word)-1 && !ptr.Terminal {
			return false
		}
	}
	return true
}

func (this *Trie) StartsWith(prefix string) bool {
	ptr := this

	for _, char := range prefix {
		if _, ok := ptr.Children[string(char)]; !ok {
			return false
		}
		ptr = ptr.Children[string(char)]
	}
	return true
}

func (this *Trie) Print(curr string, currNode *Trie) {
	if currNode.Terminal {
		fmt.Println("WORD:", curr)
		for k, _ := range currNode.Children {
			fmt.Println(k)
		}
	}
	for k, v := range currNode.Children {
		this.Print(curr+string(k), v)
	}
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */

func main() {
	obj := Constructor()
	obj.Insert("apple")
	param_2 := obj.Search("apple")
	param_3 := obj.Search("app")
	param_4 := obj.StartsWith("app")
	obj.Insert("app")
	param_5 := obj.Search("app")
	fmt.Println([]bool{
		param_2,
		param_3,
		param_4,
		param_5,
	})
	obj.Print("", &obj)
	// for k, _ := range obj.Children {
	// 	fmt.Println(k)
	// }

	// for _, char := range "Hello_World!" {
	// 	fmt.Println(string(char))
	// }
}
