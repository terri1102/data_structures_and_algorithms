프로그래머스 코딩테스트 연습
https://programmers.co.kr/learn/courses/30/lessons/42576

## 첫 번째 풀이
```python
def solution(participant, completion):
    for i in participant:
        if i not in completion:
            answer = i
        if (participant.count(i) > 1) & (participant.count(i) > completion.count(i)):
            answer = i
    return answer
```
결과: 테스트 케이스 통과했다고 해서 제출했는데, 두번째 테스트에서 시간초과됨

테스트 1 〉	통과 (0.01ms, 10.2MB)

테스트 2 〉	통과 (0.04ms, 10.2MB)

테스트 3 〉	통과 (10.42ms, 10.3MB)

테스트 4 〉	통과 (40.09ms, 10.5MB)

테스트 5 〉	통과 (39.02ms, 10.5MB)

## 두 번째 풀이
```python
def solution(participant, completion):
    for i in participant:
        if (participant.count(i) > completion.count(i)):
            answer = i
    return answer
```

결과: 역시 실패...약간은 빨라 진 것 같다.
테스트 1 〉	통과 (0.01ms, 10.2MB)

테스트 2 〉	통과 (0.02ms, 10.1MB)

테스트 3 〉	통과 (5.69ms, 10.3MB)

테스트 4 〉	통과 (22.39ms, 10.3MB)

테스트 5 〉	통과 (21.02ms, 10.3MB)

## 다른 사람 풀이 1
```python
def solution(participant, completion): 
    hash ={} 
    for i in participant: 
        if i in hash: 
            hash[i] += 1 
        else: 
            hash[i] = 1 
    for i in completion: 
        if hash[i] == 1: 
            del hash[i] 
        else: 
            hash[i] -= 1 
    answer = list(hash.keys())[0] 
    return answer
```


## 다른 사람 풀이 2
```python
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```
