from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(1, numRows+1):
            if i < 3:
                answer.append([1 for _ in range(i)])
            else:
                prev_list = answer[i-2]
                curr_list = []
                for j in range(i):
                    if (j == 0) or (j == i - 1):
                        curr_list.append(1)
                    else:
                        num = prev_list[j-1] + prev_list[j]
                        curr_list.append(num)
                answer.append(curr_list)
        return answer

if __name__ == "__main__":
    case1 = [1, 2, 3, 4, 10, 30]
    s = Solution()
    for case in case1:
       print(s.generate(case)) 

