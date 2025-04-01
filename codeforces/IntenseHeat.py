# https://codeforces.com/contest/1003/problem/C

n, k = map(int, input().split())
P = list(map(int, input().split()))

PS = [0] * (n+1)
for i in range(1, n+1):
    PS[i] = PS[i-1] + P[i-1]

res = 0
for i in range(n-k+1):
    for j in range(i+k, n+1):
        if res < (PS[j] - PS[i]) / (j-i):
            res = (PS[j] - PS[i]) / (j-i)

print(res)

'''
line 14: max 함수 대신에 if를 활용하니 시간초과 해결
'''
