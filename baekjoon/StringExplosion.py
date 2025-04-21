import sys
input = sys.stdin.readline

P = input().strip()
B = input().strip()

bl = len(B)
s = []
for p in P:
    s.append(p)
    if ''.join(s[-bl:]) == B:
        del s[-bl:]

if not s:
    print("FRULA")
else: 
    print(''.join(s))

'''9935
# 문자열 폭발 - stack
 -> 문자 하나씩 push하다가 뒤쪽 끝이 Bomb 문자열과 똑같으면 del.
'''
