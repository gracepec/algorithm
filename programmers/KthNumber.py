def solution(A, C):
    res = []
    for c in C:
        i = c[0]
        j = c[1]
        k = c[2]
        
        An = A[i-1:j]
        An.sort()
        
        res.append(An[k-1])
    
    return res

''' 42748
# 배열을 자르고 정렬하여 k번째 수 구하기 - sort
'''
