from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int, input().split())

M = [[0] * col for _ in range(row)]
for r in range(row):
    ln = input()
    for c in range(col):
        M[r][c] = int(ln[c])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

cnt = 0
possible = False
V = [[[False] * col for _ in range(row)] for _ in range(2)]
q = deque([(0,0,0,cnt)]) # b는 벽 부순 여부 F:0, T:1
V[0][0][0] = True
while q:
    cr, cc, b, cnt = q.popleft()
    if cr == row-1 and cc == col-1:
        possible = True
        break
    # print(cr,cc, b)
    for i in range(4):
        nr, nc = cr+dr[i], cc+dc[i]
        if 0 <= nr < row and 0 <= nc < col:
            if M[nr][nc] == 0 and not V[b][nr][nc]:
                q.append((nr, nc, b, cnt+1))
                V[b][nr][nc] = True
            elif M[nr][nc] == 1 and b == 0 and not V[1][nr][nc]:
                q.append((nr, nc, 1, cnt+1))
                V[1][nr][nc] = True

print(cnt+1 if possible else -1)

''' 2206
# 벽 부수고 이동하기(하나까지 부술수있음) - BFS
    -> Visited를 한개가 아닌 두개(3차원)로 구분해야 최단이 가능
'''
