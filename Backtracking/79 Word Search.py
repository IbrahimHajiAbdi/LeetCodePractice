from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        for i in word:
            if not any(i in sublist for sublist in board):
                return False
        def recurse(board: List[List[str]], curr: str, y: int, x: int, seen: List[tuple]) -> bool:
            if curr == word:   
                return True
            if not word.startswith(curr):
                return False
            if y >= len(board) or x >= len(board[0]) or y < 0 or x < 0:
                return False
            if (y, x) in seen:
                return False
            curr += board[y][x]
            seen.append((y, x))
            return (
                recurse(board, curr, y+1, x, seen[:]) or
                recurse(board, curr, y-1, x, seen[:]) or
                recurse(board, curr, y, x+1, seen[:]) or
                recurse(board, curr, y, x-1, seen[:]) 
            )                  
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    y = i
                    x = j
                    res = recurse(board, "", y, x, [])
                    if res: return res
        return res
    
sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
print(sol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAa"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

