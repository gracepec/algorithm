def solution(A):
    S = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    R = [0] * 3
    for i in range(3):
        l = (len(A) // len(S[i])) + 1
        S[i] *= l
        
        for a, s in zip(A, S[i]):
            if a == s:
                R[i] += 1
                
    T = []
    m = max(R)
    for i in range(3):
        if R[i] == m:
            T.append(i+1)
    
    return T

''' 42840
# 수포자가 찍은 번호로 문제를 제일 많이 맞춘사람 찾기 - brute force
'''
