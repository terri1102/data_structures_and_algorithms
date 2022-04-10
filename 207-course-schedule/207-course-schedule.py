class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
        # print(graph) [[], [0]]
        
    
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            
            # visit all the neighbors
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        
         #visit each node
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True