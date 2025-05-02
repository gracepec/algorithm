from collections import deque
import sys
input = sys.stdin.readline

G = [i for i in range(101)]

n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    G[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    G[u] = v

V = [False] * 101
q = deque([(1,0)])
while q:
    cn, cnt = q.popleft()
    V[cn] = True
    if cn == 100:
        print(cnt)
        break
    for i in range(1,7):
        if cn+i <= 100 and not V[G[cn+i]]:
            q.append((G[cn+i], cnt + 1))
            V[G[cn+i]] = True
                
''' 16928
# 뱀과 사다리 게임에서 100에 가장 빠르게 도달하는 법 - BFS

G: 그래프를 1~100까지 보드판으로 생성한 뒤 건너뛰는 부분은 그 숫자로 기입
-> 주사위 범위 1~6을 더해보며 100에 도달하는 가장 빠른 횟수 구함 (BFS)
    cnt를 q에 튜플로 (현재위치와) 같이 넣어야 그 경우의 수로 구해짐
    시간복잡도, 공간복잡도 O(1)
'''
