# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())
G = [tuple(map(int, input().split())) for _ in range(n)]

G.sort(key=lambda x: (x[1], x[0]))

e = 0
res = 0
for start, end in G: 
    if start >= e:
        e = end
        res += 1

print(res)

"""
# 시작과 끝 시간을 받아서 최대한 많이 회의실 배정 - 그리디

sort(key=lambda x: (x[1], x[0])) : 두번째(끝시간) 원소 기준으로 정렬
"""
