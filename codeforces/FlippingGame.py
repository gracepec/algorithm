# https://codeforces.com/contest/327/problem/A

n = int(input())
P = list(map(int, input().split()))

so = P.count(1)
mf = -1

A = [0] * n
for i, p in enumerate(P):
    A[i] = 1 if p == 0 else -1

D = [0] * n
for i in range(n):
    D[i] = max(D[i-1] + A[i], A[i])
    mf = max(mf, D[i])

print(so + mf)


'''
result: max_flip을 계산해 처음 sum_one에 더한 값

A: 0과 1을 1,-1로 변환
D: DP배열에 최대부분합을 저장
mf: 최종 최대부분합
'''
