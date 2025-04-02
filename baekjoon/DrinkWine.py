# https://www.acmicpc.net/problem/2156

n = int(input())
P = [int(input()) for _ in range(n)]

P.append(0)
D = [0] * (n+2)
for i in range(n):
    D[i] = max(D[i-1], D[i-2]+P[i], D[i-3]+P[i-1]+P[i])
    
print(D[n-1])

'''
# 연속된 3개는 선택할 수 없는 최대 합 구하기
'''
