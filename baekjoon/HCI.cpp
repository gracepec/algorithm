#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    string S;
    int s, i, c, n, l, r, cn;
    char ch;
    
    cin >> S;
    s = S.size();

    vector<vector<int>> D(26, vector<int>(s+1, 0));
    for (i = 1; i <= s; i++) {
        for (c = 0; c < 26; c++) {
            if (c == S[i-1]-'a') 
                D[c][i] = D[c][i-1] + 1;
            else
                D[c][i] = D[c][i-1];
        }
    }

    cin >> n;
    while (n--) {
        cin >> ch >> l >> r;
        cn =  ch - 'a';
        cout << D[cn][r+1] - D[cn][l] << "\n";
    }
        
    return 0;
}
