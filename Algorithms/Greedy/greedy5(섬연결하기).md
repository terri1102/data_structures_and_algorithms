## 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/42861
## 문제 설명
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

## 제한사항

섬의 개수 n은 1 이상 100 이하입니다.

costs의 길이는 ((n-1) * n) / 2이하입니다.

임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.

같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.

모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.

연결할 수 없는 섬은 주어지지 않습니다.

## 입출력 예

|n|	costs|	return|
|---|---|---|
|4|	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	| 4|

## 풀이
크루스칼 알고리즘과 최소 신장 트리 개념을 알아야 함

1) 정렬
2) 사이클을 형성하지 않는 간선 선택
```python
n =4
answer = 0
costs = 	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
costs.sort(key= lambda x: x[2]) #비용 기준 오름차순 정리
connect = set([costs[0][0]]) #{0}

#Kruskal 알고리즘으로 최소 비용 구하기
while len(connect) != n:
    for cost in costs: #cost는 [0,1,1] 이런식의 리스트
        if cost[0] in connect and cost[1] in connect: 
            continue
        if cost[0] in connect or cost[1] in connect: 
            connect.update([cost[0], cost[1]])
            answer += cost[2]
print(answer)
def solution(n, costs):
    answer = 0
    #1. 그래프의 모든 에지를 최소힙 H에 추가
    costs.sort(key = lambda x: x[2]) #최소힙 H. 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 최소 신장 트리 T. 연결을 확인하는 집합 
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
    #2. 최소 힙(H)으로부터 에지 e를 하나 꺼냄. 모든 에지 중 가중치가 가장 작은 에지
        for cost in costs:
    #3. 에지 e의 양 끝 정점이 이미 T에 있으면 사이클이 발생. 이럴 경우 e를 버리고 다음 단계로.
            if cost[0] in connect and cost[1] in connect: ##이미 두 섬이 연결되었을 때. 즉 섬 1이 connect에 있고, 섬 2가 connect에 있을 때 넘어가기
                continue
    #4. 최소 신장트리 T에 e를 추가하고, 2단계로 이동
            if cost[0] in connect or cost[1] in connect: ##둘 중 하나의 섬이 connect에 있을 때. connect에 {0}이 있으니까 이걸 시작점으로 잡는 듯
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer
```

풀이 출처

https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-python
