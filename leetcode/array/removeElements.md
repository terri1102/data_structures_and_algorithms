https://leetcode.com/problems/remove-element/submissions/

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val) > 0:
            nums.remove(val)
            nums.append('_')
        nums = [i for i in nums if type(i) == int]
        return len(nums)

```
