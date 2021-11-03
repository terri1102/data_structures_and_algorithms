## 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42860

## 문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳

▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)

◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)

▶ - 커서를 오른쪽으로 이동

## 입출력 예
|name	|return|
| :---: | :---: |
|"JEROEN"|	56 |
|"JAN" |	23 |

## 풀이
min을 써서 굉장히 깔끔하게 풀었다.
1) 문자열 조작
2) 커서 조작
```python
def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer
```


## 내 풀이
일단 내가 푼 풀이는 테스트케이스 3,4,5,7,11 통과 못함

문제를 제대로 안 읽어서 문자 개수만큼 A로 이루어졌다는 걸 고려 못함.

또한 커서를 왼쪽으로 이동하는 경우를 생각 못 해서 그런 것 같다.

```python
def solution(name):
    answer = 0
    for char in name:
        alpha_num = 0
        ord_name = ord(char)
        alpha = ord_name - 65
        if ord_name <= 77: #A에서부터 올림(M이 77)
            alpha_num = alpha
            if char == "A":
                answer -= 1 #A면 커서 이동 안 함
        elif ord_name > 77: #Z에서부터 내림
            alpha_num = 91 - ord_name  
            print(char, alpha_num)
        #print(char, ord_name, alpha_num)
        answer += alpha_num
    
    answer += len(name) - 1
    return answer
```
