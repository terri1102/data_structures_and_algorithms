from collections import defaultdict
def solution(edges):
    answer = []
    graph = defaultdict(list)
    for src, dst in edges:
            graph[src].append(dst)
    visited = set()
    donut = []
    path = []
    def dfs(node):
        nonlocal path
        nonlocal visited
        if node in graph:
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    path.append(next_node)       
                    dfs(next_node)
                else:
                    for node in path:
                        pass # if donut; donut.append(path)
                        # if stick; stick.append(path)
                        # if eight; eight.append(path)
                    path = []
            else:
                return
    start_node = edges[0][0]
    donut = []
    stick = []
    eight = []
    
    for node in graph.keys():
        dfs(node)

    
    return answer
if __name__ == "__main__":
    sample2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    sample1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
    print(solution(sample1))
    print(solution(sample2))

