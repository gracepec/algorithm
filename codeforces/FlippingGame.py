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

maxi = A.index(max(A))
mini = A.index(min(A))
df = max(A) - min(A)

res = A.count(1) + df

print(res)
