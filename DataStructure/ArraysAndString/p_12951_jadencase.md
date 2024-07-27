## 문제 JadenCase
https://school.programmers.co.kr/learn/courses/30/lessons/12951


## 아이디어
스트링 전체 순회하기
1. 스트링을 리스트로 변환(공백이 보존됨)
2. 순회하면서 isFirst flag로 첫 번째 문자인지 확인
- prev_char가 " "이고 현재 char가 alphanumeric이면 isFirst
3. isFirst면서 alphabet이면 upper()로 대문자 변환,
아니면 lower()로 소문자 변환
4. 변환된 리스트를 다시 스트링으로 join

![problem](jadencase.jpeg)

## 풀이
```python
def solution(s):
    if not s:
        return s
    
    prev_char = " "
    isFirst = True
    s_array = [a for a in s]
    
    for i, char in enumerate(s_array):
        if prev_char == " " and char.isalnum():
            isFirst = True
        else:
            isFirst = False
        if char.isalpha():
            if isFirst is True:
                s_array[i] = char.upper()
            else:
                s_array[i] = char.lower()
        prev_char = char
    
    answer = "".join(s_array)
        
    return answer
```

## 배운 점
- string을 split()으로 나누면 공백 여러 개인 경우 구분 못함
- isalpha(): 알파벳인지(A-Za-z) 확인
- isdigit(): 숫자인지 확인. 
- isnumeric(): 숫자인지 확인. Superscript(위 첨자), subscript, 분수, 로마자 등 더 넓은 범위의 숫자 포함. ex) Ⅳ,½, ²
- isalnum(): 알파벳인지 숫자인지 확인
- isspace(): 공백인지 확인


```python
def solution(s):
    preFlag = ''
    s_array = [c for c in s]
    for i in range(len(s_array)):
        if i == 0:
            preFlag = s_array[i]

            if preFlag.isalpha():
                s_array[i] = s_array[i].upper()
        else:
            cur = s_array[i]
            
            if cur.isalpha():
                if preFlag == ' ':
                    s_array[i] = s_array[i].upper()
                else:
                    s_array[i] = s_array[i].lower()

            preFlag = cur
            
    answer = ''.join(s_array)
        
    return answer

def solution(s):
    if not s:
        return s
    
    prev_char = " "
    isFirst = True
    s_array = [a for a in s]
    
    for i, char in enumerate(s_array):
        if prev_char == " " and char.isalnum():
            isFirst = True
        else:
            isFirst = False
        if char.isalpha():
            if isFirst is True:
                s_array[i] = char.upper()
            else:
                s_array[i] = char.lower()
        prev_char = char
    
    answer = "".join(s_array)
        
    return answer


if __name__ == "__main__":
    s = '  What    what'
    print(solution(s))
```

# for문이 아니라 map으로도 풀어보기
#''.join(map(lambda x: x.capitalize(), s.split(" ")))

# capitalize 함수: 첫 번째 단어는 대문자로, 나머지는 소문자로
# 범위가 1000까지여서 O(n^2)여도 되겠다고 판단 -> 완전탐색
# 범위가 10만...이러면 보통 시간 초과

# 파이썬 internals 공부가 더 필요함
# split()
# strings = "d dk  kdj   d"
# result = strings.split(" ")
# print(result)  # Output: ['d', 'dk', '', 'kdj', '', '', 'd']
