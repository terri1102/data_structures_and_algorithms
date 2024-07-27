from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # Initialize the grid and scale up by 2 to avoid fractional coordinates
    grid_size = 102
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # Draw the rectangles on the grid, marking the outline
    for rect in rectangle:
        x1, y1, x2, y2 = [2 * coord for coord in rect]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    grid[x][y] = 2  # Inside the rectangle
                elif grid[x][y] != 2:
                    grid[x][y] = 1  # Outline of the rectangle

    # BFS setup
    start = (characterX * 2, characterY * 2)
    end = (itemX * 2, itemY * 2)
    queue = deque([start])
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS
    distance = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return distance // 2  # Divide by 2 to get original distance
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[nx][ny] == 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        distance += 1

    return -1  # Just a safety return, problem guarantees a solution

# Example test case
rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
characterX, characterY = 1, 3
itemX, itemY = 7, 8
print(solution(rectangle, characterX, characterY, itemX, itemY))  # Output: 17
