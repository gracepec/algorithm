# https://www.acmicpc.net/problem/4949

import sys

def solve(P):
    S = [-1]
    for p in P:
        if p ==')' and S[-1] != 0:
            return "no"
        if p ==']' and S[-1] != 1:
            return "no"
        if p == '(':
            S.append(0)
        if p == ')' and S[-1] == 0: #
            S.pop()
        if p == '[':
            S.append(1)
        if p == ']' and S[-1] == 1: #
            S.pop()
    if len(S) == 1:
        return "yes"
    return "no"

while (line := input()) != '.':
    P = list(line)
    print(solve(P))

'''
# 괄호 균형이 잘 맞는지 확인 문제

:= (왈러스 연산자) -> 입력과 비교를 동시에 처리 ver3.8 이상
    """ 기본
        while true:
            line = input()
            if line == '.':
                break
            P = list(line)
    """
'''
