# https://leetcode.com/problems/missing-number/
from typing import List

class Solution:
    def missingNumber_sort(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return num

    def missingNumber_hashset(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            hash_set.add(num)
        for i in range(len(nums)+1):
            if i not in hash_set:
                return i
    
    def missingNumber_bitops(self, nums: List[int]) -> int:
        k = len(nums)
        for i, num in enumerate(nums):
            tmp = i ^ num
            k ^= tmp
        return k

    def missingNumber_sum(self, nums: List[int]) -> int:
        total = (len(nums) * (len(nums)+1)) // 2
        nums_sum = sum(nums)
        return total - nums_sum



