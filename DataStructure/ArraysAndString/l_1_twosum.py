# https://leetcode.com/problems/two-sum/description/

def solution(array, target):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
  
                return [i, j]

def solution_hash(array, target):
    element_hash = {}

    for i, i_num in enumerate(array):
        # element_hash[i_num] = i
        # if i_num in element_hash:
        next_ele = target - i_num
        if next_ele in element_hash:
            return [element_hash[next_ele], i]
        else:
            element_hash[i_num] = i

if __name__ == "__main__":
    sample1 = [0, 3, 5, 7, 10]
    target = 8
    print(solution(sample1, target))
    print(solution_hash(sample1, target))
