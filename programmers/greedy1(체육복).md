## 문제 
https://programmers.co.kr/learn/courses/30/lessons/42862

## 문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

## 제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

## 입출력의 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5

## 풀이1
```python
def solution(n, lost, reserve):
    answer = 0 
    answer = n - len(lost)
    
    lost.sort()
    reserve.sort()
    
    D = [i for i in lost if i in reserve] #lost와 reserve 둘 다에 포함된 학생
    
    for d in D:
        lost.remove(d) #lost에서 제거
        reserve.remove(d) #reserve에서도 제거
    answer += len(D) #lost였던 학생이 옷 입게 된 거니까...len(D)를 더해줌
    
    
    for i in lost:
        if i-1 in reserve: #앞 사람
            reserve.remove(i-1) 
            answer += 1
        elif i+1 in reserve: #뒷 사람
            reserve.remove(i+1)
            answer += 1

    return answer

```

## 풀이2
테스트케이스 18번과 20번 통과가 안 된다! 
f와 b에 둘 다 있을 때 remove 쓰면 문제 생기는 거 같다...
나의 경우 학생 배열, lost_arr, reserve_arr를 다 만들어서 풀려고 했는데, 
그러면 앞 뒤만 빌려주는 부분은 또 따로 구현을 해야 해서 다른 분들 풀이가 더 나은 거 같다.

```python
def solution(n, lost, reserve):
    _lost = [l for l in lost if l not in reserve] #reserve가 없는 진짜 체육복이 없는 학생 구하기
    _reserve = [r for r in reserve if r not in lost] #lost에 없는 진짜 체육복이 남는 학생 구하기
    
    for r in _reserve:
        f = r - 1 #여분의 체육복 있는 사람의 앞 사람
        b = r + 1 #여분의 체육복 있는 사람의 뒷 사람
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
    
```
