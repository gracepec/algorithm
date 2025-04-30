from collections import deque
import sys
input = sys.stdin.readline

n, e, sn = map(int, input().split())

G = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for g in G:
    g.sort()

V = [False] * (n+1)
def dfs(cn):
    V[cn] = True
    Res.append(cn)
    for nn in G[cn]:
        if not V[nn]:
            dfs(nn)
            
def bfs(sn):
    V = [False] * (n+1)
    q = deque([sn])
    while q:
        cn = q.popleft()
        V[cn] = True
        Res.append(cn)
        for nn in G[cn]:
            if not V[nn] and not nn in q:
                q.append(nn)
    
Res = []
dfs(sn)
print(" ".join(map(str, Res)))

Res = []
bfs(sn)
print(" ".join(map(str, Res)))

''' 1260
sn: start node
cn: current node
nn: next node
V: Visited bool
G: Graph
'''
