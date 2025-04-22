# https://www.acmicpc.net/problem/11286

import sys
import heapq

input = sys.stdin.readline
n = int(input())

h = []
for _ in range(n):
    p = int(input())
    if p != 0:
        heapq.heappush(h, (abs(p),p))
    else:
        if h: 
            print(heapq.heappop(h)[1])
        else: 
            print(0)

'''
# 절대값 힙 - heap
'''
