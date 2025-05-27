import sys
input = sys.stdin.readline

while True:
    N = input().strip()
    if N == '':
        break
    else:
        N = int(N)
        
    cn = 3**N
    C = ['-'] * cn

    def cutMid(l, r):
        tri = (r-l+1) // 3
        for i in range(tri):
            C[l + tri + i] = ' '

        if tri > 1:
            cutMid(l, l+tri)
            cutMid(l+tri*2, r)

    cutMid(0, cn)
    print(''.join(C))

''' 4779
# 칸토어 집합: 주어진 N으로 3**N의 길이에 '-' 중 가운데 부분을 잘라내어 
    모든 선의 길이가 1이 되면 출력 - Recursion
'''
