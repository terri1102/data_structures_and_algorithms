# https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math



def solution(arrayA, arrayB):
    answer = 0
    # Case1
    max_a = max(arrayA)
    for num in arrayA:
        for i in range(2, math.sqrt(max_a)):
            if num % i == 0 and i >= answer:
                answer = i
    for num in arrayB:
        if num % answer == 0:
            answer = 0
    if answer != 0:
        return answer
    # Case2
    max_b = max(arrayB)
    for num in arrayB:
        for i in range(2, math.sqrt(max_b)):
            if num % i == 0 and i >= answer:
                answer = i
    for num in arrayA:
        if num % answer == 0:
            answer = 0
    return answer

