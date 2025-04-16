import sys
input = sys.stdin.readline

n, maxw = map(int, input().split())
W = [0] * n
V = [0] * n
for i in range(n):
    W[i], V[i] = map(int, input().split())

D = [0] * (maxw+1)
for i in range(n):
    for wi in range(maxw, W[i]-1, -1):
        D[wi] = max(D[wi], V[i] + D[wi-W[i]])

print(D[maxw])

'''12865
# 배낭문제 - DP
 배낭 최대무게(maxw)까지 Dynamic 배열 생성 - 인덱스(wi)를 무게로 활용
 각 원소에는 해당 무게(W)에서 가질 수 있는 최대의 가치(V)로 업데이트
 뒤에서 부터 업데이트 해야 본인이 중복되지 않고 한번씩만 포함될 수 있음
 
1) [ 0 0 0 0 0 13 13 ]
2) [ 0 0 0 8 8 13 13 ]
3) [ 0 0 6 8 8 13 14 ]
4) [ 0 0 6 8 12 13 14 ]

    """ 2차원 배열로 풀기 (메모리, 시간 효율 떨어짐)
        W = [0] * (n+1)
        V = [0] * (n+1)
        for i in range(1, n+1):
            W[i], V[i] = map(int, input().split())
        
        D = [[0] * (maxw+1) for _ in range(n)]
        for i in range(n):
            for wi in range(maxw+1):
                if wi < W[i]:
                    D[i][wi] = D[i-1][wi]
                else:
                    D[i][wi] = max(D[i-1][wi],  D[i-1][wi-W[i]] + V[i])
            
        print(D[n-1][maxw])
    """
'''
