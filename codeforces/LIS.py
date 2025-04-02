# https://www.acmicpc.net/problem/11053

from bisect import bisect_left

n = int(input())
P = list(map(int, input().split()))

L = [-1]
for i in range(n):
    lidx = bisect_left(L, P[i])
    if lidx == len(L):
        L.append(P[i])
    if lidx < len(L):
        L[lidx] = P[i]

res = len(L) - 1
print(res)

'''
bisect_left(A, x): A 배열에서 x보다 크거나 같은 첫 번째 인덱스 반환
        -> LIS 배열에서 가장 왼쪽 위치를 반환 (이진탐색 O(log N))
'''
