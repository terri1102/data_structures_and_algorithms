## 문제 1512. Number of Good Pairs

## 출처
https://leetcode.com/problems/number-of-good-pairs/submissions/

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            else:
                hash_map[nums[i]] += 1
        return sum(k * (k + 1) // 2 for k in hash_map.values())

```
