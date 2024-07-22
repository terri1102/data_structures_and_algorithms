from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        answer = []
        i = 0 
        while i < len(intervals): # 0, 1, 2 # 항상 헷갈림
            if answer:
                curr_list = answer[-1]
            else:
                curr_list = intervals[i]
            # if curr_list[1] < intervals[i][0]:
                answer.append(intervals[i])
                i += 1
                continue
            while (i < len(intervals)) and (curr_list[1] >= intervals[i][0]):
                # if intervals[i][0] <= curr_list[1]:
                curr_list[1] = max(curr_list[1], intervals[i][1])
                i += 1
            if i < len(intervals):
                answer.append(intervals[i])
            # breakpoint()
        return answer


if __name__ == "__main__":
    case1 = [[1, 3], [2, 6], [8, 10], [15, 18]]  # Expected: [[1, 6], [8, 10], [15, 18]]
    case2 = [[1, 3], [2, 5], [3, 7], [6, 10], [9, 13], [14, 15], [15, 18]]  # Expected: [[1, 13], [14, 18]]
    case3 = [[2,3], [5,6], [6,7], [8,10]]
    s = Solution()
    print(s.merge(case1))
    print(s.merge(case2))
    print(s.merge(case3))

