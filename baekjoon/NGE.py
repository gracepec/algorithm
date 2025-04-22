import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))

P.append(0)
S = []
for i in range(n):
    if P[i] > P[i-1]:
        S.append((i, P[i]))
print(S)

res = [0] * n
pb = False
for i in range(n):
    for s in S:
        if s[0] <= i:
            pb = True
        if s[1] > P[i]:
            res[i] = s[1]
        print(i, s, res[i], S)
    if pb and S:
        S.pop(0)
    if res[i] == 0:
         res[i] = -1

print(res)

'''17298
# 오큰수(오른쪽에 있으면서 큰 수 중 가장 왼쪽(가까이)에 있는 수) - stack
'''
