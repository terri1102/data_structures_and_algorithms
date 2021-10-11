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
해시테이블을 이용해서 O(n)으로 풀었다. 근데 내 풀이도 O(n)인듯??
```python
def twosum(nums, target):
    hashtable_dict = {}
    
    for i in range(0, len(nums)):
        value = target - nums[i]
        
        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
            return sorted([i, hashtable_dict[value]])
            
            
        hashtable_dict[nums[i]] = i
        
    return [-1, -1]
```
