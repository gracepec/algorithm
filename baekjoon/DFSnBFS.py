from collections import deque
import sys
input = sys.stdin.readline

n, e, sn = map(int, input().split())

G = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

V = [False] * (n+1)
Res = []
def dfs(cn):
    V[cn] = True
    Res.append(cn)
    for nn in G[cn]:
        if not V[nn]:
            dfs(nn)
            
def bfs(sn):
    V = [False] * (n+1)
    V[sn] = True
    Res = []
    q = deque([sn])
    while q:
        cn = q.popleft()
        V[cn] = True
        Res.append(cn)
        for nn in G[cn]:
            if not V[nn]:
                q.append(nn)
    
    
dfs(1)
print(Res)

bfs(1)
print(Res)

''' 1260
'''
