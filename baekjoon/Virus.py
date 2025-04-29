import sys
input = sys.stdin.readline

n = int(input()) + 1
t = int(input())

G = [[] for _ in range(n)]
for _ in range(t):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

V = [False] * n
def dfs(nn, cnt):
    V[nn] = True
    for g in G[nn]:
        if not V[g]:
            cnt = dfs(g, cnt+1)
    return cnt

print(dfs(1, 0))

''' 2606
# 1번에서 연결된 노드 개수 구하기 - graph, dfs

dfs(G, V, nn, cnt)로 쓰지 않아도 되는 이유는
 -> 파이썬에서 list는 참조를 사용하는 mutable 객체이기 때문에.

*bfs로도 풀이 가능
    """BFS
        V = [False] * n
        def bfs(sn):
            q = deque([sn])
            V[1] = True
            cnt = 0
            
            while q:
                cn = q.popleft()
                for nn in G[cn]:
                    if not V[nn]:
                        V[nn] = True
                        q.append(nn)
                        cnt += 1
            return cnt
                    
        print(bfs(1))
    """
'''
