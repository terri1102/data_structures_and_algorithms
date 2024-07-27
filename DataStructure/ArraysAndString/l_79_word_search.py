# https://leetcode.com/problems/word-search/description/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols or word[i] != board[row][col] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            for dr, dc in directions:
                if dfs(row + dr, col + dc, i + 1):
                    return True
            visited.remove((row, col))
            return False
        
        for i in range(num_rows):
            for j in range(num_cols):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    board = [["A","B","col","E"],["S","F","col","S"],["A","D","E","E"]]
    word = "ABCCED"
    board2 = [["A","B","col","E"],["S","F","col","S"],["A","D","E","E"]]
    word2 = "SEE"
    print(s.exist(board, word))  # True
    print(s.exist(board2, word2))  # True

# 아래 풀이는 백트레킹이 잘 이루어지지 않았음

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
        
#         visited = set()
#         word_index = 0
#         answer = False  
#         direction = [(1, 0), (0,1), (-1, 0), (0, -1)]
       
#         def dfs(curr_loc):
#             nonlocal word_index
#             nonlocal visited
#             nonlocal answer
#             if word_index == len(word) - 1:
#                 answer = True
#                 return
#             for i in range(len(direction)):
#                 new_loc = (curr_loc[0] + direction[i][0], curr_loc[1] + direction[i][1])
#                 if (0 <= new_loc[0] < len(board)) and (0 <= new_loc[1] < len(board[0])) and (new_loc not in visited):
#                     if board[new_loc[0]][new_loc[1]] == word[word_index]:
#                         visited.add(new_loc)
#                         word_index += 1
                        
#                         if word_index == len(word) - 1:
#                             answer = True
#                             return
#                         dfs(new_loc)
#                     else:
#                         word_index -= 1 
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[word_index]:
#                     visited.add((i,j))
#                     word_index += 1
#                     while (word_index < len(word)) and (answer == False):
#                         dfs((i, j))

#                 visited = set()
#                 word_index = 0
#                 answer = False  
    
#         return answer
           
if __name__ == "__main__":
    s = Solution() # 6
    board = [["A","B","col","E"],["S","F","col","S"],["A","D","E","E"]]
    word = "ABCCED"
    board2 = [["A","B","col","E"],["S","F","col","S"],["A","D","E","E"]]
    word2 = "SEE"
    print(s.exist(board, word))
    print(s.exist(board2, word2))