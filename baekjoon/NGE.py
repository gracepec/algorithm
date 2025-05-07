import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))

S = []
Res = []
for p in reversed(P):
    while S and S[-1] <= p:
        S.pop()
    Res.append(S[-1] if S else -1)
    S.append(p)
    
print(*reversed(Res))
    
'''17298
# 오큰수(오른쪽에 있으면서 큰 수 중 가장 왼쪽(가까이)에 있는 수) - stack
'''
