import heapq
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
M = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [0] * 10005
fi = 10
for i in range(n):
    for ci in range(fi, -1, -1):
        if D[fi] != 0:
            D[fi+C[i]] = max(D[fi+C[i]], D[fi]+M[i])
    D[C[i]] = max(D[C[i]], M[i])
print(D)

'''7579
# 

n=5 p=60
M 30 10 20 35 40
C 3  0  3  5  4

  0  3  3  4  5
  10 20 30 40 35
D [0][1][2][3][4]
0 10 
1 
2 
3     30 40
4           50
5              45
6        60  <- P랑 크거나같 나오면 이 아래 계산할 필요 X
7          (80)
8
9
10        (100X)

0이 아니면 초기화x 

'''
