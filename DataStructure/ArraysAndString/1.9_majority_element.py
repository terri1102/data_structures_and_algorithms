import math
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        max_num = max(counter.values())
        for k, v in counter.items():
            if v == max_num:
                return k

    def majorityElement2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        nums_len = len(nums)
        counter = 0
        prev_num = nums[0]
        for i in nums[1:]:
            if prev_num == i:
                counter += 1
            else:
                prev_num = i 
                counter = 1

            if counter >= math.ceil(nums_len/2):
                return i

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,3]
    nums2 = [2,1,2,2,1,1,3,2,4,2,2] 
    nums3 = [2]
    print(s.majorityElement(nums))
    print(s.majorityElement(nums2))
    print(s.majorityElement(nums3))

    print(s.majorityElement2(nums))
    print(s.majorityElement2(nums2))
    print(s.majorityElement2(nums3))

