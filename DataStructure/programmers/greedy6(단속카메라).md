## 문제 링크
https://programmers.co.kr/learn/courses/30/lessons/42884

## 문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

## 제한사항

차량의 대수는 1대 이상 10,000대 이하입니다.

routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.

차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.

차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

## 입출력 예

|routes |	return |
|---|---|
|[[-20,-15], [-14,-5], [-18,-13], [-5,-3]] |	2|


## 풀이
작업 스케줄링 문제와 일부 비슷함.

1. 종료 시간(차량이 나간 지점) 기준으로 정렬
2. 가장 빠른 종료 시간을 갖는 작업 선택
3. 현재 선택된 작업과 시간이 겹치는 작업 모두 제거
4. 리스트에 작업이 남아 있으면 2단계로 이동. 그렇지 않으면 반환.
```python
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾음

    for route in routes:
        if camera < route[0]: #차량 진입점보다 카메라 앞에 있으면
            answer += 1
            camera = route[1] #차량 나간 지점에 카메라 추가
    return answer
```


출처: https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
