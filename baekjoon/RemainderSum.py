import sys
input = sys.stdin.readline

n, m = map(int, input().split())
P = list(map(int, input().split()))

D = [0] * n
for i in range(n):
    D[i] = D[i-1] + P[i]

res = 0
for i in range(n):
    for j in range(i, n):
        print(j,i, D[j] - D[i])
        if (D[j] - D[i]) % m == 0:
            res += 1
print(res)

'''10986
# 나머지 합 - prefix sum

p 1 2 3 1 2
D 1 3 6 7 9


'''
