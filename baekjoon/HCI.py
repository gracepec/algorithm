# https://www.acmicpc.net/problem/25501

import sys
input = sys.stdin.readline

S = input().strip()
s = len(S)
D = [[0] * (s+1) for _ in range(26)]
for i in range(s):
    for c in range(26):
        D[c][i] = D[c][i-1] + (1 if c == ord(S[i])-ord('a') else 0)

n = int(input())
for _ in range(n):
    ch, l, r = input().split()
    ch = ord(ch) - ord('a')
    l, r = int(l), int(r)
    
    print(D[ch][r] - D[ch][l-1])

'''
# l, r 사이 특정 알파벳이 몇 번 나타나는지 구하는 문제 (50점) - prefix sum
    (PyPy3 언어로 제출 시 100점 sol)

ord() : 문자(char) ASCII 변환(int) 
ex) ord('c') - ord('a') == 2

    """ dict 활용한 새로운 알파벳 나오면 저장
        D = {}
        for _ in range(n):
            ch, l, r = input().split()
            l, r = int(l), int(r)
            
            if ch not in D:
                D[ch] = [0] * (s+1)
                for i in range(s):
                    D[ch][i] = D[ch][i-1] + (1 if S[i] == ch else 0)
        
            print(D[ch][r] - D[ch][l-1])
    """
'''
