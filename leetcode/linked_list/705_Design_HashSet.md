## 문제  705. Design HashSet

## 출처
https://leetcode.com/problems/design-hashset/submissions/

## 풀이
built-in function을 쓰지 말라는 말을 듣자..!

문제 설명은 내일의 나에게 맡긴다
https://leetcode.com/problems/design-hashset/discuss/768659/Python-Easy-Multiplicative-Hash-explained

아래 코드에서 사용한 해시 함수는 multiplicative hash 인데
먼저 

```python
class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]

```
