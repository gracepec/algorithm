def solution(P, C):
    P.sort()
    C.sort()

    for p, c in zip(P, C):
        if p != c:
            return p
    return P[-1]

'''42576
# 완주하지 못한 선수 찾기(마라톤) - hash
 -> 정렬 후 하나씩 zip()으로 매칭
    같지 않은 원소가 완주하지 못한 선수 리턴
    끝까지 없다면 남은 선수 리턴
    
    """ Counter 활용
        from collections import Counter

        def solution(P, C):
            return list((Counter(P) - Counter(C)).keys())[0]
    """
'''
