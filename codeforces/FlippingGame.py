# https://codeforces.com/contest/327/problem/A

n = int(input())
C = list(map(int, input().split()))

A = [0] * n

dt = 0
for i in range(n):
    if C[i] == 1:
        dt += 1
    if C[i] == 0:
        dt -= 1
    A[i] = dt
print(A)
maxi = A.index(max(A))
mini = n-1 - list(reversed(A)).index(min(A))

if maxi == 0 and C[0] == 0: 
    maxi = -1

print(maxi+1, mini+1)

for i in range(maxi+1, mini+1):
    C[i] = 1 - C[i]
print(C)
res = C.count(1)

print(res)

# progress in
# 9
# 1 1 0 0 1 0 1 1 1
