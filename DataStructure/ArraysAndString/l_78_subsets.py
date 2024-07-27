from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        def subsets_recursion(nums: List[int], res: List[List[int]], sub: List[int], index) -> None:
            if len(sub) > len(nums):
                return
            
            res.append(sub.copy())

            for i in range(index, len(nums)):
                sub.append(nums[i])
                subsets_recurson(nums, res, sub, i + 1)
                sub.pop()
            
            subsets_recursion(nums, res, sub, index)
if __name__ == "__main__":
    s = Solution()
    case1 = [1,2,3,4]
    print(s.subsets(case1))
