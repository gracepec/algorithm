from collections import deque
import sys
input = sys.stdin.readline

col, row = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(row)]

q = deque()
for r in range(row):
    for c in range(col):
        if B[r][c] == 1:
            q.append((r,c))

Dr = [-1,1,0,0]
Dc = [0,0,-1,1]
while q:
    r,c = q.popleft()
    for i in range(4):
        nr, nc = r+Dr[i], c+Dc[i]
        if 0 <= nr < row and 0 <= nc < col and B[nr][nc] == 0:
            q.append((nr, nc))
            B[nr][nc] = B[r][c] + 1
                
# print(*B, sep='\n')
res = max(map(max, B)) - 1
for b in B:
    if 0 in b:
        res = -1
        
print(res)

''' 7576
# 상자에 인접한 토마토가 점점 익어가는 최단 경로 구하기 - BFS (시작점 여러개)
'''
