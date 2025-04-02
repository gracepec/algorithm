# https://www.acmicpc.net/problem/1912

n = int(input())
P = list(map(int, input().split()))

res = 0
D = [0] * n
D[0] = P[0]
for i in range(1, n):
    D[i] = max(D[i-1] + P[i], P[i])

res = max(D)
print(res)

'''
# 구간 연속합 최대 구하기
'''
