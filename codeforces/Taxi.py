# https://codeforces.com/contest/158/problem/B

n = int(input())
S = list(map(int, input().split()))

G = [0, S.count(1), S.count(2), S.count(3), S.count(4)]

res = G[4] + G[3]
res += G[2] // 2
G[2] = G[2] % 2
G[1] = max(0, G[1] - G[3])

if G[2] == 1:
    res += 1
    G[1] = max(0, G[1] - 2)

res += G[1] // 4
if G[1] % 4 > 0:
		res += 1

print(res)