def solution(n, L, R):
    Ls = set(L) - set(R)
    Rs = set(R) - set(L)
    
    for r in sorted(Rs):
        if r-1 in Ls:
            Ls.remove(r-1)
        elif r+1 in Ls:
            Ls.remove(r+1)
            
    return n - len(Ls)

''' 42862
# 체육복 빌려주기 옆번호만 가능 - (greedy)

 -* 주의: 처음 중복된 값을 제거할 때 새로운 변수(Ls) 사용안하면 변경된 L 참조
 set: 중복을 허용하지 않는 집합 -> 중복원소를 차집합으로 제거하는 활용
'''
