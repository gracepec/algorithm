import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
ind = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    ind[b] += 1

H = []
for i in range(1, n+1):
    if ind[i] == 0:
        heapq.heappush(H, i)

Res = []
while H:
    cn = heapq.heappop(H)
    Res.append(cn)
    for nn in G[cn]:
        ind[nn] -= 1
        if ind[nn] == 0:
            heapq.heappush(H, nn)

print(*Res)

''' 1766
# 위상정렬 + 작은 숫자 우선 -> 진입차수(BFS) + 우선순위 큐(heap)

dfs로는 불가 (보장x)
'''
