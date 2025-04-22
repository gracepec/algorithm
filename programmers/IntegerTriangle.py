def solution(T):
    D = [[0] * len(T) for _ in range(len(T))]
    D[0][0] = T[0][0]
    
    for i in range(1, len(D)):
        for j in range(len(T[i])):
            D[i][j] = T[i][j] + max(D[i-1][j], D[i-1][j-1])
    
    return max(D[len(T)-1])
    
''' 43105
# 정수 삼각형에서 아래 두개로만 내려오며 거쳐가는 수의 합의 최대값 찾기 - DP (2차원)
'''
