from collections import deque

def solution(n, E):
    G = [[] for _ in range(n+1)]
    for a, b in E:
        G[a].append(b)
        G[b].append(a)
                
    Res = [0] * (n+1)
    V = [False] * (n+1)
    V[1] = True
    
    q = deque([(1, 0)])
    while q:
        cn, dist = q.popleft()
        Res[cn] = dist
        
        for nn in G[cn]:
            if not V[nn]:
                V[nn] = True
                q.append((nn, dist+1))
                
    return Res.count(max(Res))

''' 49189
# 1에서 가장 먼 노드 개수 구하기 - Graph, BFS
 -> G: 입력으로 받는 edge(E)로 만든 양방향 그래프 (각 인덱스가 노드번호이며, 내부 배열이 연결된 노드들)
    Res[i]: 1번 노드에서 각 i 노드들까지의 최단거리
    V: 순회(BFS)하며 방문했던 노드인지 체크하기 위한 bool list (각 인덱스가 노드번호)
    q: BFS를 위한 튜플 큐. (노드번호, 거리)
    
    * 방문한 노드의 인접을 모두 q에 넣고, 순서대로 방문해야 bfs만족 (for문 없이 하나씩 pop하면 dfs:최단거리x)
'''
