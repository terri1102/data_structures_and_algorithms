## 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/43236

## 문제 설명
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
```
[21, 17]	[2, 9, 3, 11]	2
[2, 21]	[11, 3, 3, 8]	3
[2, 11]	[14, 3, 4, 4]	3
[11, 21]	[2, 12, 3, 8]	2
[2, 14]	[11, 6, 4, 4]	4
```
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

## 제한사항
도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.

바위는 1개 이상 50,000개 이하가 있습니다.

n 은 1 이상 바위의 개수 이하입니다.

## 입출력 예
|distance|	rocks|	n|	return|
|25|	[2, 14, 11, 21, 17]|	2|	4|

## 풀이
여기서 이분 탐색의 기준: 돌과 돌 사이의 거리

1. 돌과 돌 사이 거리가 기준 값보다 작으면 뒤쪽 돌 삭제
2. 삭제한 돌의 개수가 기준 n보다 클 경우 돌과 돌 사이의 거리를 줄이고, n보다 작거나 같을 경우 거리를 늘리는 식으로 진행

```python
import math
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance) # 전체 거리
    left, right = 0, distance

    #바위 사이 최소 거리보다 거리가 작을 경우 돌 삭제
    # 거리가 클 경우, 이 값들 중 최솟값을 구해둠

    answer = 0
    while left <= right:
        #이전 돌
        prev_rock = 0
        #돌 거리 최솟값
        mins = math.inf
        #제거한 돌 개수
        removed_rocks = 0

        #바위 사이의 최소거리
        mid = (left+right) //2
        #각 돌을 돌면서 제거할 돌을 찾음
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed_rocks += 1
            else:
                mins = min(mins, rocks[i] - prev_rock )
                prev = rocks[i]

        #제거한 돌 개수가 기준보다 많다 = 바위 제거를 줄인다
        # 바위 사이 최소 거리 기준을 낮춰야 한다
        if removed_rocks > n:
            right = mid -1
        
        else:
            answer = mins
            left = mid + 1
    return answer

```



풀이 출처: https://m.post.naver.com/viewer/postView.nhn?volumeNo=27217004&memberNo=33264526
