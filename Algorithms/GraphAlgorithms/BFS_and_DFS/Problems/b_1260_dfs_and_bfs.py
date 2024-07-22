# https://www.acmicpc.net/problem/1260

## 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque, defaultdict

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = {node: False for node in graph}
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 그래프 입력 처리
n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색을 위한 방문 기록 딕셔너리
visited = {node: False for node in range(1, n + 1)}

# DFS 실행
dfs(graph, v, visited)
print()

# BFS 실행
bfs(graph, v)
