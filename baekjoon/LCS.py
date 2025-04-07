# https://www.acmicpc.net/problem/9251

P = input()
Q = input()

n, m = len(P), len(Q)
D = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if P[i] == Q[j]:
            D[i+1][j+1] = D[i][j] + 1
        else:
            D[i+1][j+1] = max(D[i][j+1], D[i+1][j])

print(D[n][m])

'''
# LCS : 최장 공통 부분 수열
ex) ACAYKP, CAPCAK => 4(ACAK)
'''
