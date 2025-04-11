# https://www.acmicpc.net/problem/2696

import sys
import heapq

input = sys.stdin.readline
inputs = sys.stdin.read

t = int(input())
for _ in range(t):
    maxh = []
    minh = []
    
    n = int(input())
    if n <= 10: ###### 
        P = list(map(int, input().split()))
    else:
        P = list(map(int, inputs().split())) # 라인수 명시 필요

    od = n // 2 + 1
    print(od)
    mid = [0] * (od)
    
    heapq.heappush(maxh, -P[0])
    mid[0] = P[0]
    for i in range(1, n):
        if not minh or P[i] > -maxh[0]:
            heapq.heappush(minh, P[i])
        elif P[i] <= -maxh[0]:
            heapq.heappush(maxh, -P[i])

        if len(minh) >= len(maxh) + 2: 
            heapq.heappush(maxh, -heapq.heappop(minh))
        elif len(minh) < len(maxh):
            heapq.heappush(minh, -heapq.heappop(maxh))
        
        if i % 2 == 0:
            mid[i // 2] = minh[0]
            
    for i in range(0, n, 10):
        print(*mid[i:i+10])

'''
# 중앙값 구하기 - 이중힙
""" 런타임에러 """
'''
