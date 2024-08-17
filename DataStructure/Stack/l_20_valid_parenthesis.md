# 문제: 20. Valid Parenthesis

## 아이디어
- 같은 종류의 괄호가 닫혀야 하기 때문에 스택 자료 구조 사용
- valid_set 딕셔너리를 만들어서 valid한지 확인

## 풀이
1. 스택 초기화
2. 괄호 쌍이 맞는지 확인할 valid_set 딕셔너리 생성
3. s의 char별로 순회하면서 스택 마지막 요소와 쌍이 맞는지 확인

3-1. 만약 쌍이 맞으면 스택에서 pop

3-2. 쌍이 맞지 않으면 스택에 char push

3-3. 스택이 비어있다면 char를 스택에 push

4. s를 모두 순회 후에 스택이 비어있으면 True, 비어있지 않으면 False 리턴

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # valid_set = {"{":"}", "}":"{", "(": ")", ")":"(", "[":"]", "]":"["}
        valid_set = {"{":"}",  "(": ")", "[":"]"}
        for char in s:
            if stack:
                curr = stack[-1]
                if curr in valid_set and char != valid_set[curr]:
                    stack.append(char)
                elif curr in valid_set and char == valid_set[curr]:
                    stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        # (){}}{
        return True
```

## 배운 점
- valid_set 을 만들 때 시작 괄호만 키로 넣어야 `(){}}{` 같은 경우를 false로 처리할 수 있다.