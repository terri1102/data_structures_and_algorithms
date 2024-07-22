def solution(n, results):
    # 그래프 초기화
    can_defeat = [[False] * n for _ in range(n)]
    
    # 경기 결과 입력
    for winner, loser in results:
        can_defeat[winner-1][loser-1] = True
    
    # 플로이드-워셜 알고리즘 적용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if can_defeat[i][k] and can_defeat[k][j]:
                    can_defeat[i][j] = True
    print(can_defeat)
if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))
