# https://www.acmicpc.net/problem/1904

n = int(input())

D = [0] * (n+1)
D[1] = 1
if n > 1 : 
    D[2] = 2

for i in range(3, n+1):
    D[i] = (D[i-1] + D[i-2]) % 15746

print(D[n])

'''
피보나치 수열이 된다는 아이디어 혹은 발견
memory -> 나머지 연산을 반복문 안에서 계산
'''
