from typing import List
def mergeTwoIntervals(array1: List[List[float]], array2: List[List[float]]) -> List[List[float]]:
    if len(array1) == 0 and len(array2) > 0:
        return array2
    elif len(array1) == 0 and len(array2) == 0:
        return array1
    elif len(array1) == 0 and len(array2) == 0:
        return [[]]

    i = 0
    j = 0
    answer = []

    while i < len(array1): # and j < len(array2):
        if answer:
            prev_list = answer[-1]
        else:
            prev_list = array1[i]
            answer.append(prev_list)
            i += 1


        while (i < len(array1)) and (j < len(array2)) and ((prev_list[1] >= array2[j][0]) or (prev_list[1] >= array1[i][0])):
            if prev_list[1] >= array2[j][0]:
                prev_list[1] = max(prev_list[1], array2[j][1])
                j +=1
            elif prev_list[1] >= array1[i][0]:
                prev_list[1] = max(prev_list[1], array1[i][1])
                i += 1

        if i < len(array1):
            answer.append(prev_list)

    if j < len(array2):
        for j in range(j, len(array2)):
            answer.append(array[j])
            j += 1
    return answer

if __name__ == "__main__":
    case1_a1, case1_a2 = [[1,2], [3,5],[7,8]], [[1,3], [4.5, 6.0], [9,10]]
    print(mergeTwoIntervals(case1_a1, case1_a2))
