# https://codeforces.com/contest/1003/problem/C

n, k = map(int, input().split())
P = list(map(int, input().split()))

PS = [0] * (n+1)
for i in range(1, n+1):
    PS[i] = PS[i-1] + P[i-1]

res = 0
for i in range(n-k+1):
    for j in range(i+k, n+1):
        res = max(res, (PS[j] - PS[i]) / (j-i))
        
print(res)

'''
Time Limit Exceeded (n = 5000)

but is okay for cpp
    """
        #include <iostream>
    
        using namespace std;
        
        int main() {
            int P[5005];
            int PS[5005];
        
            int n, k, i, j;
            double res;
        
            cin >> n >> k;
        
            P[0] = 0;
            for (i = 1; i <= n; i++) {
                cin >> P[i];
                PS[i] = PS[i-1] + P[i];
            }
        
            res = 0.0;
            for (i = 0; i < n-k+1; i++) {
                for (j = i+k; j < n+1; j++) {
                    res = max(res, double(PS[j] - PS[i]) / double(j-i));
                }
            }
        
            printf("%lf\n", res);
        
            return 0;
        }
    """
'''
