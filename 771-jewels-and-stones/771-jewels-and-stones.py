class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map = {}
        for char in jewels:
            for s in stones:
                if char == s:
                    if char not in hash_map:
                        hash_map[char] = 1
                    else:
                        hash_map[char] += 1
        return sum(hash_map.values())
                
        