## 문제 771. Jewels and Stones

## 출처
https://leetcode.com/problems/jewels-and-stones/submissions/

## 내 풀이
이중 루프인 것이 아쉽다...
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map = {}
        for char in jewels:
            for s in stones:
                if char == s:
                    if char not in hash_map:
                        hash_map[char] = 1
                    else:
                        hash_map[char] += 1
        return sum(hash_map.values())

```

## 다른 풀이
깔끔하지만 위의 풀이보다 느리다
```
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
```
