def solution(strings, n):
    return sorted(strings, lambda x: (x[n], x))

