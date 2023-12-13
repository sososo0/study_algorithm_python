# study_algorithm_python

python으로 algorithm 공부 

### BFS 

- **사용하는 자료 구조 : Queue**
- **사전 지식 : 레벨 탐색** (출발 상태에서 도착 상태까지 최소 횟수의 상태 변화로 도착 상태까지 가는 상태 횟수 찾기)

### DFS 

- **사용하는 자료 구조 : Stack**
- **사전 지식 : 중복 순열**

### Graph 

- **사전 지식 : 인접 리스트**

### Sort 

파이썬 내장 정렬 함수 쓰는 것이 시간적으로 가장 좋음 
```
array = [3,1,2]
array.sort()
```

- **선택 정렬** : 처리되지 않은 데이터 중에서 맨 앞의 데이터가 가장 작은 데이터와 순서 변경
- **삽입 정렬** : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- **퀵 정렬** : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법, 첫 번째 데이터를 기준 데이터(pivot)으로 설정
- **계수 정렬** : 데이터(양수) 중 최대값 K를 찾아 K+1 길이의 리스트를 생성, 해당 리스트를 통해 데이터들의 개수를 Count한 후, 리스트에 Counting된 수 만큼 출력 
- **버블 정렬** : 뒤에서 부터 앞으로 정렬을 해나가는 구조, 맨 뒷자리에 제일 큰 값을 제일 뒤로 보내는 방식으로 정렬 
[bubble sort](https://www.daleseo.com/sort-bubble/)

### Greedy 

- 현재 상황에서 지금 당장 좋은 것만 고르는 방법으로 현재의 선택이 나중에 미칠 영향에 대해서는 생각하지 않음
- 따라서, 최적의 해는 보장하지 않음 
- Greedy로 접근했을 때 최적의 해를 구할 수 있다는 보장이 있는 경우에는 매우 효과적이고 직관적

### Two Pointers

- 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미 
- 리스트에 담긴 데이터를 시작점과 끝점 2개의 점으로 접근할 데이터의 범위로 표현할 수 있음 ex. [1, 2, 3, 4, 5, 6]에서 3부터 5 

[참고 강의 1](https://school.programmers.co.kr/learn/courses/14760/14760-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%99%80-%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94-pccp-%ED%95%A9%EA%B2%A9-%EB%8C%80%EB%B9%84-%EC%8B%A4%EC%A0%84-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-%ED%95%B4%EC%84%A4-%EA%B0%95%EC%9D%98python%ED%8E%B8) 

[참고 강의 2](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)