## 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/43165

## 문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

## 입출력 예
|numbers|	target|	return|
|---|---|---|
|[1, 1, 1, 1, 1]|	3|	5|


## BFS 풀이
```python
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0]) #numbers의 첫번째 element +
    queue.append([-1*numbers[0],0]) #numbers의 첫번째 element - . deque([[1,0],[-1,0]]) 이런식으로 들어가게 됨
    while queue:
        temp, idx = queue.popleft()
        idx += 1 #다음 원소 선택
        if idx < n:
            queue.append([temp+numbers[idx],idx]) #numbers의 원소 + 그 다음 위치의 원소
            queue.append([temp - numbers[idx],idx]) #numbers의 원소 - 그 다음 위치의 원소
            print(queue)
        else:
            if temp == target:
                answer += 1
    return answer
```

## DFS 풀이

```python
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer
```

풀이 출처 : https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS
