# 가장 빠른 경로를 찾는 것이기 때문에 BFS로 풀어야 함!!!
# DFS로 풂면 효율성 테스트에서 실패함
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    
    queue = deque([(0, 0, 1)])
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        row, col, dist = queue.popleft()
        
        if row == n - 1 and col == m - 1:
            return dist
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < n and 0 <= new_col < m:
                if maps[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, dist + 1))

    return -1

def solution222(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    directions = [ [1, 0], [0, 1], [0,-1], [-1,0]] 
    answer = 1
    answers = []
    queue = deque([(0, 0)])
    while queue:
        curr_row, curr_col = queue.popleft()
        for move in directions:
            row = curr_row + move[0]
            col = curr_col + move[1]
            if  (0 <= row < n) and (0 <= col < m):
                if (maps[row][col] == 1) and (not visited[row][col]):
                    visited[row][col] = True
                    answer += 1
                    if row == n-1 and col == m-1:
                        answers.append(answer)
                    
                    queue.append((row, col))


def solution2(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    # directions = [[-1,0], [1, 0], [0,-1], [0, 1]] # U, D, L, R
    directions = [ [1, 0], [0, 1], [0,-1], [-1,0]] # D, R, L, U
    answers = []
    def dfs(curr_row, curr_column, answer):
        nonlocal visited
        for move in directions:
            row = curr_row + move[0]
            column = curr_column + move[1]
            if  (0 <= row < n) and (0 <= column < m):
                if (maps[row][column] == 1) and (not visited[row][column]):
                    visited[row][column] = True
                    answer += 1
                    # print(row, column, answer)
                    if row == n - 1 and column == m - 1:
                        answers.append(answer)
                        # answer -= 1
                        # visited[row][column] = False
                    else:
                        dfs(row, column, answer)
                    answer -= 1
                    visited[row][column] = False

        return -1

    dfs(0,0,1)
    if answers:
        # print(answers)
        answer = min(answers)
        return answer
    else:
        return -1


if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))
    maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    print(solution(maps2))
