from collections import defaultdict

def solution(arrows):
    answer = 0
    edges = []
    curr_loc = [0, 0]
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)] 
    for arrow in arrows:
        x, y = direction[arrow]
        curr_loc[0] = curr_loc[0] + x
        curr_loc[1] = curr_loc[1] + y
        edges.append((curr_loc[0], curr_loc[1]))
    
    def dfs(v, parent):
        nonlocal cycle_count
        visited[v] = True
        for neighbor in adjacency_list[v]:
            if not visited[neighbor]:
                parent_map[neighbor] = v
                dfs(neighbor, v)
            elif neighbor != parent: # iscycle
                cycle_count += 1

    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    visited = {}
    parent_map = {}
    cycle_count = 0

    for node in adjacency_list:
        visited[node] = False

    for node in adjacency_list:
        if not visited[node]:
            dfs(node, -1)
    answer = cycle_count // 2
    return answer

if __name__ == "__main__":
    arrows_input = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
    print(solution(arrows_input))

