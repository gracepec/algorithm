def solution(S):
    l = []
    r = []
    for s in S:
        if s[0] >= s[1]:
            l.append(s[0])
            r.append(s[1])
        else:
            r.append(s[0])
            l.append(s[1])
        
    return max(l) * max(r)
            
''' 86491
# 가로세로 명함 길이를 받아서 다 들어가는 최소 지갑 크기 출력 - 완전탐색(Brute-Force)
'''
