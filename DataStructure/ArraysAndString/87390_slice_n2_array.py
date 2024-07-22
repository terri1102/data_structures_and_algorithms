# https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        row = i // n
        col = i % n
        curr = max(row, col) + 1

        answer.append(curr)
    return answer

