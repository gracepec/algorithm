import sys
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
    bi = True
    V = [False] * (ver+1)
    def dfs(cn):
        global bi, res
        for nn in G[cn]:
            if V[nn] and V[cn][1] == V[nn][1]:
                res = "NO"
            if not V[nn]:
                bi = False if bi else True
                V[nn] = (True, 0 if bi else 1)
                dfs(nn)
                bi = False if bi else True
            
    dfs(1)
    print(res)
