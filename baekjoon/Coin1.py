import sys
input = sys.stdin.readline

n, k = map(int, input().split())
V = [int(input()) for _ in range(n)]

D = [0] * (k+1)
D[0] = 1
for v in V:
    for vi in range(v, k+1):
        D[vi] += D[vi-v]
print(D[k])

'''2293
# 동전 조합 경우의 수 문제 - DP

v: 동전의 가치
vi: 동적배열의 인덱스이자 가치
 -> 값에 해당 가치를 만들 수 있는 경우의 수 업데이트

ex) 
    3 5
    1\n2\n5
    
    D = []
     0 1 2 3 4 5 : vi
    [1 1 1 1 1 1] : v=1
    [1 1 2 2 3 3] : v=2
    [1 1 2 2 3 4] : v=5
    
    1- 1
    2- 11 2 
    3- 111 12
    4- 1111 112 22
    5- 11111 1112 122 5
'''
