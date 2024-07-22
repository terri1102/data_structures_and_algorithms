# Cracking coding interviews
# 4.1 방향 그래프가 주어졌을 때 두 노드 사이 경로가 존재하는지 확인
# - 함수 argument: node1, node2
# 예시 
from collections import defaultdict, deque
input = ["A C", "A E", "B A", "B D", "E D"]

# 1. 그래프 구현
graph = defaultdict(list)

visited = {}
for edge in input:
    start, end = edge.split()
    graph[start].append(end)
    if start not in visited:
        visited[start] = False
    if end not in visited:
        visited[end] = False

# 2. BFS
def solution(v1, v2):
    if v1 == v2:
        return True
    queue = deque([v1])
    while queue:
        temp = queue.popleft()
        if not visited[temp]:
            visited[temp] = True
            if temp == v2:
                return True
            for node in graph[temp]:
                queue.append(node)
    return False        
print(graph)
print(solution("A", "D"))
print(solution("D", "A"))
