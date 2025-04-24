from functools import cmp_to_key

def compare(a, b):
    return (int(b+a) > int(a+b)) - (int(b+a) < int(a+b))

def solution(P):
    P = list(map(str, P))
    P.sort(key=cmp_to_key(compare))
    
    return ''.join(P) if P[0] != '0' else '0'

''' 42746
# 수 배열을 문자로 이어붙여 만들 수 있는 가장 큰 수 구하기 - sort

cmp_to_key(f): f(a,b)를 key 함수로 바꿔주는 역할
'''
