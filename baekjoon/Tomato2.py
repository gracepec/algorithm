from collections import deque
import sys
input = sys.stdin.readline

col, row, depth = map(int, input().split())
B = [[list(map(int, input().split())) for _ in range(row)] for _ in range(depth)]

q = deque()
for d in range(depth):
    for r in range(row):
        for c in range(col):
            if B[d][r][c] == 1:
                q.append((d,r,c))

Dd = [-1,1,0,0,0,0]
Dr = [0,0,-1,1,0,0]
Dc = [0,0,0,0,-1,1]
while q:
    d,r,c = q.popleft()
    for i in range(6):
        nd, nr, nc = d+Dd[i], r+Dr[i], c+Dc[i]
        if 0<= nd < depth and 0 <= nr < row and 0 <= nc < col and B[nd][nr][nc] == 0:
            q.append((nd, nr, nc))
            B[nd][nr][nc] = B[d][r][c] + 1

res = 0
for bb in B:
    for b in bb:
        if 0 in b:
            print(-1)
            sys.exit()
        res = max(res, max(b))
print(res-1)

''' 7569
# 토마토 익히기 3차원 - BFS, 3D array
'''
