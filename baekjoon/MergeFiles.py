import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    P = list(map(int, input().split()))
    
    H = []
    res = 0
    heapq.heapify(P)
    while len(P) + len(H) > 1:
        print(sorted(P) ,H) ########################
        while len(P) > 1:
            s = heapq.heappop(P) + heapq.heappop(P)
            heapq.heappush(H, s);
            res += s
        if len(P) == 1:
            s = heapq.heappop(P)
            heapq.heappush(H, s)
            res += s
        print(P ,H) ########################
        while len(H) > 1:
            s = heapq.heappop(H) + heapq.heappop(H)
            heapq.heappush(P, s);
            res += P[0]
        if len(H) == 1:
            s = heapq.heappop(H)
            heapq.heappush(P, s)
            res += P[0]
        print(P ,H) ########################
        print("t",res) ###########
    print(res)

'''11066

 1 2 3 4 5
  3  +7 
   +8 
    +15
33

3 5 7 [3+7]
7 8 [+8]
15 +
= 33 min

'''

