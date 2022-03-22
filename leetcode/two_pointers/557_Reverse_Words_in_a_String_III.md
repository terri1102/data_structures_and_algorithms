## 문제

## 출처
https://leetcode.com/problems/reverse-words-in-a-string-iii/

## 내 풀이

이렇게 풀면 안 될 것 같은 방법으로 풀었다...

왜냐면 two pointer 방법으로 하니까 자꾸 인덱스 에러나서
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 단어별 알파벳 순서 바꾸기
        s_list = s.split()
        res = []
        for word in s_list:
            print("".join(reversed(word))) ## "".join 안 하면 reversed 객체임
            res.append("".join(reversed(word)))
        return " ".join(res)

```

```python
def reverseWords_manual(s):  # O(n) both
    res = ''
    l, r = 0, 0
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r + 1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]

```
