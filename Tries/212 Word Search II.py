from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Solution:
    def insert(self, root: TrieNode, word: str):
        ptr = root

        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]

        ptr.terminal = True  

    def printTrie(self, root: TrieNode, currStr: str):
        if root.terminal:
            print("WORD:", currStr)
        for k, v in root.children.items():
            self.printTrie(v, currStr + k)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: 
        trie = TrieNode()
        seen = set()
        all_words = set()

        for word in words:
            self.insert(trie, word)
        
        def findWordsRecursive(y: int, x: int, currNode: TrieNode, currStr: str):
            if currNode.terminal and currStr not in all_words:
                    all_words.add(currStr)
                    # return True
            if y >= len(board) or x >= len(board[0]) or y < 0 or x < 0:
                return False
            if (y, x) in seen:
                return False
            if board[y][x] in currNode.children:
                currStr += board[y][x] 
                seen.add((y, x))
                res =  (
                    findWordsRecursive(y + 1, x, currNode.children[board[y][x]], currStr[:]) or
                    findWordsRecursive(y - 1, x, currNode.children[board[y][x]], currStr[:]) or 
                    findWordsRecursive(y, x + 1, currNode.children[board[y][x]], currStr[:]) or
                    findWordsRecursive(y, x - 1, currNode.children[board[y][x]], currStr[:])
                )

                seen.remove((y, x))
                return (
                    res
                )
            else:
                return False
        for y in range(len(board)):
            for x in range(len(board[0])):
                findWordsRecursive(y, x, trie, "")
        return list(all_words)
            
sol = Solution()
print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]))