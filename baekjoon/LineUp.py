import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

Res = []
V = [False] * (n+1)
def dfs(cn):
    V[cn] = True
    for nn in G[cn]:
        if not V[nn]:
            dfs(nn)
    Res.append(cn)

for i in range(1, n+1):
    if not V[i]:
        dfs(i)
        
print(*reversed(Res))

''' 2252
# 위상정렬(방향 그래프 줄 세우기) - graph, dfs
    -> dfs 기반 후의 순회 + 역순 출력

bfs로도 가능 -> in-degree 방식 (진입차수)
'''
