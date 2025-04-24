def solution(P, S):
    F = []
    for p, s in zip(P, S):
        F.append((100-p) // s + (1 if (100-p) % s != 0 else 0))
    
    Res = [1]
    idx = 0
    cur = F[0]
    for f in F[1:]:
        if f <= cur:
            Res[idx] += 1
        else:
            Res.append(1)
            idx += 1
            cur = f
    
    return Res

''' 42586
# 기능개발 (%와 속도 주어지고 몇개씩 배포(완료)될지) - list
'''
