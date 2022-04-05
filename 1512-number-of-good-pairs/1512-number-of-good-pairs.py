from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        "two sum이랑 같은 문제 아녀"
        
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            else:
                hash_map[nums[i]] += 1

        cnt = 0
        for d in hash_map.values():
            cnt += comb(d+1,2)

        return cnt
        