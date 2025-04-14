import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    maxh = []
    minh = []
    
    n = int(input())
    P = []
    for _ in range((n - 1) // 10 + 1):
        P += list(map(int, input().split()))

    mid = []
    for i, x in enumerate(P):
        if not maxh or x <= -maxh[0]:
            heapq.heappush(maxh, -x)
        else:
            heapq.heappush(minh, x)

        if len(maxh) > len(minh) + 1:
            heapq.heappush(minh, -heapq.heappop(maxh))
        elif len(minh) > len(maxh):
            heapq.heappush(maxh, -heapq.heappop(minh))

        if i % 2 == 0:
            mid.append(-maxh[0])

    print(len(mid))
    for i in range(0, len(mid), 10):
        print(*mid[i:i+10])

''' 2696
# 중앙값 구하기 - 이중힙
'''
