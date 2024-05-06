# BFS(Breadth-first-search)

BFS는 트리 순회 알고리즘으로 root 노드에서 한 depth를 다 서치한 후에 다음 depth로 넘어가서 서치하는 알고리즘이다.

## 구현
queue를 통해서 depth별로 queue에 넣은 다음에 pop해서 순회한다.
```python
from collections import deque, defaultdict
def bfs(graph, start):
    # Initialize
    queue = deque([start])
    visited = set([start])
    result = []
    while queue:
        next_node = queue.popleft()
        result.append(next_node)
        for node in graph[next_node]:
            if node not in visited:
                queue.append(node)
                visited.add(node)

    return result

if __name__ == "__main__":
    n, m, v = 5, 6, 1
    graph = defaultdict(list)
    edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4],[2,5]]
    for (a, b) in edges:
        graph[a].append(b)
        graph[b].append(a)
    print("Graph: ", graph)

    print("BFS traversal:", bfs(graph, v))

    # 1, 2, 3, 4, 5


```

### 시간 복잡도
O(V+E)

### 공간 복잡도

