def dfs(T, V, cn, cnt):
    V[cn] = True
    for nn in T[cn]:
        if not V[nn]:
            cnt = dfs(T, V, nn, cnt+1)
    return cnt
    
def solution(n, wires):
    G = [[] for _ in range(n+1)]
    for a, b in wires:
        G[a].append(b)
        G[b].append(a)
            
    ans = float('inf')
    for a, b in wires:
        T = [g[:] for g in G]
        T[a].remove(b)
        T[b].remove(a)
        
        V = [False] * (n+1)
        vis = dfs(T, V, 1, 1)

        ans = min(ans, abs(n-vis*2))
        
    return ans

'''86971
# 전력망(트리) 둘로 나누기(최대한 개수 비슷하게) - Graph, dfs, bf
'''
