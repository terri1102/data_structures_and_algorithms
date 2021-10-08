## 내가 푼 풀이

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other_half = target - nums[i]
            if other_half in nums[i+1:]:
                if other_half != nums[i]:
                    return [i, nums.index(other_half)]
                else:
                    p_list = [i for i,x in enumerate(nums) if x==other_half]
                    return [i, p_list[1]]
```

## 책 풀이
