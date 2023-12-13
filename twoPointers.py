# data 리스트에서 부분합 m을 반복하는 경우의 수 구하기 
n = 5
m = 5

data = [1, 2, 3, 2, 5]

cnt = 0
end = 0
numSum = 0

for start in range(n):
    while numSum < m and end < n:
        numSum += data[end]
        end += 1 
    if numSum == m:
        cnt += 1
    numSum -= data[start]

print(cnt)
