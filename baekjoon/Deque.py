# https://www.acmicpc.net/problem/28279

import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()
for _ in range(n):
    if ' ' in (p := sys.stdin.readline()):
        P = list(map(int, p.split()))
        p = P[0]
    else: p = int(p)
    
    if p == 1:
        dq.appendleft(P[1])
    elif p == 2:
        dq.append(P[1])
    elif p == 3:
        print(dq.popleft()) if dq else print(-1)
    elif p == 4:
        print(dq.pop()) if dq else print(-1)
    elif p == 5:
        print(len(dq))
    elif p == 6:
        print(1) if not dq else print(0)
    elif p == 7:
        print(dq[0]) if dq else print(-1)
    elif p == 8:
        print(dq[-1]) if dq else print(-1)

'''
# 덱 사용 기본 문제

반복문 속 input()사용 : 시간초과
  -> sys.stdin.read()
  """ 현재 코드가 아래 보다 300ms 빠름 (왈러스 활용)
      for _ in range(n):
        P = list(map(int, sys.stdin.readline().split()))
        p = P[0]
  """
'''
