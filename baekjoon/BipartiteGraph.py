import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tc = int(input())
for i in range(tc):
    ver, e = map(int, input().split())
    G = [[] for _ in range(ver+1)]
    for i in range(e):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    res = "YES"
    V = [-1] * (ver+1)
    def dfs(cn, pnt):
        global res
        V[cn] = pnt
        for nn in G[cn]:
            if V[nn] == -1:
                dfs(nn, 1-pnt)
            elif V[cn] == V[nn]:
                res = "NO"
                
    for i in range(1,ver+1):
        if V[i] == -1:
            dfs(i, 0)
    
    print(res)

''' 1707
# 이분 그래프가 맞는지 리턴 - graph, dfs

이분그래프는 여러 컴포넌트가 가능 (모두 연결된 그래프가 아닌) - line:25~27
sys.setrecursionlimit(10**6) : 파이썬 최대 재귀 깊이를 늘려주는
    - 기본값은 약 1,000
'''
