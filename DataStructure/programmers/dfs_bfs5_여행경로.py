from collections import deque, defaultdict
# import copy
# def solution(tickets):
#     # airports 3 - 10000
#     # 모두 사용 -> 전체 순회
#     graph = defaultdict(list)
#     for ticket in tickets:
#         a, b = ticket
#         graph[a].append(b)
#     # 재방문 가능 -> visited x
#     # 다익스트라 k 를 이용..!
#     # airports = list(set([a for b in tickets for a in b]))
#     # airports = []
#     # for ticket in tickets:
#     #     a, b = ticket 
#     #     if a not in airports:
#     #         airports.append(a)
#     #     if b not in airports:
#     #         airports.append(b)
#     # print(airports)
#     # # ICN 부터 시작해야 함
#     # graph = [[0] * len(airports) for _ in range(len(airports))]
#     # graph[0][0] = 1
#     # for ticket in tickets:
#     #     src, dst = ticket
#     #     src_idx, dst_idx = airports.index(src), airports.index(dst)
#     #     graph[src_idx][dst_idx] = 1
#     # print(graph)
#     # stack = []
#     # stack.append()
#     # for i in range(len(airports)):
#     #     for j in range(len(airports)):
#     #         for k in range(len(airports)):
#     #             if graph[i][k] == 1 and graph[k][j] == 1:
#     #                 graph[i][j] = 1
#     answer = ["ICN"]
#     answers = []
#     def dfs(graph, start):
#         nonlocal answer
#         nonlocal answers
#         if len(answer) == len(tickets) + 1:
#             ans = copy.deepcopy(answer)
#             answers.append(ans)
#             print(answers)
#             return
#         stack = []
#         for node in graph[start]:
#             stack.append(node)
#             answer.append(node)
#             dfs(graph, node)
            
#             # answer.pop(-1)
#         return answer

#     dfs(graph,"ICN")
#     print(answers)
#     new_answer = sorted([ans[1:] for ans in answers])
#     #answers.sort() # ICN 제외하고 sort해야 함
#     result = new_answer.insert(0, "ICN")
#     return result

def solution(tickets):
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)

    for src in graph:
        graph[src].sort(reverse=True)
    print(graph)
    path = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        path.append(airport)
    
    dfs("ICN")
    return path[::-1]

if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))
