## 문제 1441. Build an Array With Stack Operations
## 출처
https://leetcode.com/problems/build-an-array-with-stack-operations/submissions/

## 풀이
```python
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
        #target = [1,3]
        #n=3
        # target에 없는 숫자는 push 후 바로 pop
        
        res = []
        for i in range(1,n+1):
            if i > target[-1]: # n:4이고 target은 [1,3]인 경우
                return res
            
            if i not in target:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
        return res
        
```
