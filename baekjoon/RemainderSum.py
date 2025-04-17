import sys
input = sys.stdin.readline

n, m = map(int, input().split())
P = list(map(int, input().split()))

D = [0] * n
R = [0] * m
for i in range(n):
    D[i] = D[i-1] + P[i]
    R[D[i] % m] += 1

def combi(n,r):
    t = b = 1
    for i in range(n-r, n):
        t *= i+1
    for i in range(r):
        b *= i+1
    return t // b
    
res = R[0]
for i in range(m):
    if R[i] >= 2:
        res += combi(R[i], 2)

print(res)

'''10986
# 구간 합이 m으로 나누어 떨어지는 경우의 수 - prefix sum
 -> 모든 구간 구하면 O(n^2); 
  => (L-R) % m == 0 <==> L % m == R % m

D: prefix sum (안쓰고 바로 R만으로 가능)
R[i]: i를 나머지로 갖는 D의 개수
 -> 0은 개수만큼+1 + 같은 나머지 개수만큼 nC2 조합(combi)
'''
