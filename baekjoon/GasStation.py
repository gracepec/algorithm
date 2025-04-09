# https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
C = list(map(int, input().split()))

minc = C[0]
res = 0
for i in range(n-1):
    minc = min(minc, C[i])
    res += L[i] * minc

print(res)

"""
# 주유소를 통과하며 가장 저렴하게 끝까지 가는 방법 - 그리디
    (L: 주유소간 거리, C: 주유비)
"""
