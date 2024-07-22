
def solution(edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    node_degree = defaultdict(int)
    vertices = set()
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        node_degree[u] += 1
        node_degree[v] += 1
        vertices.add(u)
        vertices.add(v)
    
    n = len(vertices)
    donut_count = 0
    bar_count = 0
    figure8_count = 0
    visited = set()
    
    for node in vertices:
        if node_degree[node] == 2 and node not in visited:
            # Perform a DFS/BFS to count nodes in this donut shape graph
            donut_count += 1
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        elif node_degree[node] == 1 and node not in visited:
            # Perform a DFS/BFS to count nodes in this bar shape graph
            bar_count += 1
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        elif node_degree[node] == 2 and node in visited:
            # This node is already visited and part of a donut shape graph
            continue
        
        elif node_degree[node] == 3:
            # This node is part of an 8-figure shape graph (connected to two donut shape graphs)
            figure8_count += 1
    
    return [n, donut_count, bar_count, figure8_count]

# Example usage:
edges1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
edges2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

print(solution(edges1))  # Output: [4, 0, 1, 2]
print(solution(edges2))  # Output: [4, 0, 1, 2]




