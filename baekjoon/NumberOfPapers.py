# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

res = [0] * 3

def same(M):
    t = M[0][0]
    for aa in M:
        for a in aa:
            if a != t:
                return False
    res[t] += 1
    return True

def div(n, M):
    m = n // 3
    for i in range(9):
        roi = (i // 3) * m
        coi = (i % 3) * m
        Ms = [r[coi:coi+m] for r in M[roi:roi+m]]
        if not same(Ms):
            div(m, Ms)

n = int(input())
P = [[0] * n for _ in range(n)]
for i in range(n):
    P[i] = list(map(int, input().split()))

if not same(P):
    div(n, P)

print(res[-1], res[0], res[1], sep='\n')

'''
# 3^k 크기의 Metrix 에서 모든 원소가 같은 M이 나올때까지 9분할 (-1,0,1 개수 구하기)
    - 분할 정복, 재귀
'''
