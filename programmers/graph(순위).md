## 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/49191


## 문제 설명
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한사항
선수의 수는 1명 이상 100명 이하입니다.

경기 결과는 1개 이상 4,500개 이하입니다.

results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.

모든 경기 결과에는 모순이 없습니다.

## 입출력 예
|n|	results|	return|
|---|---|---|
|5|	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	|2|


## 풀이
A가 이긴 사람이 이긴 사람들은 A가 다 이긴다

```python
from collections import defaultdict
def solution(n, results):
    answer = 0
    winners = defaultdict(set)
    losers = defaultdict(set)
    
    for winner, loser in results:
        winners[loser].add(winner) #loser를 이긴 애들을 set에 넣음
        losers[winner].add(loser)
        
    for i in range(n+1):
        for winner in winners[i]:
            losers[winner].update(losers[i]) #winner가 이긴 애들에 losers[i] 추가하기
        for loser in losers[i]:
            winners[loser].update(winners[i])
    for i in range(1, n+1):
        if len(winners[i]) + len(losers[i]) == n-1: #이기거나 진 사람들이 n-1인 경우
            answer += 1
        
    return answer
        
```

풀이 출처: https://velog.io/@narastro/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-Python
