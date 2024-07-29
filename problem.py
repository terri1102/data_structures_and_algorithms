# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []
    stack1 = [(i-1, i) for i in range(n, 0, -1)]
    if n < 2:
        return [[1,3]]
    stack2 = []
    stack3 = []
    stack2.append(stack1.pop())
    answer.append([1,2])
    stack3.append(stack1.pop())
    answer.append([1,3])
    
    while len(stack3) < n - len(stack1):
    # 3번째 기둥에 가장 큰 숫자를 보내야 함    
        if stack1:
            curr = stack1.pop()
        if len(stack2) == 0:
            stack2.append(curr)
            answer.append([1, 2])
        elif len(stack3) == 0:
            stack3.append(curr)
            answer.append([1,3])
        else:
            # 빈 기둥이 없는 경우
            curr2 = stack2[-1]
            curr3 = stack3[-1]
            if curr2 < curr3:
                curr3 = stack3.pop()
                stack1.append(curr3)
                answer.append([3,1])
            elif curr3 < curr2:
                curr2 = stack2.pop()
                stack1.append(curr2)
                answer.append([2,1])


    return answer


answer = []

def hanoi(N, start, to, via):
    if N == 1:
        answer.append((start, to))
    else:
        hanoi(N-1, start, via, to)
        answer.append((start, to))
        hanoi(N-1, via, to, start)
    return answer
print(hanoi(3, 1, 3, 2))