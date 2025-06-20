import java.util.*;

class Solution {
    char[][] miro;
    char[] dirs = {'d', 'l', 'r', 'u'};
    int cnt;
    int target_cnt;
    String result = "";
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        
        miro = new char[n+2][m+2];
        for (int i = 1; i < n+1; i++) 
            for (int j = 1; j < m+1; j++)
                miro[i][j] = '.';
        
        miro[r][c] = 'e';
        cnt = 0; target_cnt = k;
        dfs(x, y);
      
        if (result == "")
            return "impossible";
        else
            return result;
    }
    
    boolean dfs(int cx, int cy) {
        if (cnt == target_cnt) {
            if (miro[cx][cy] == 'e')
                return true;
            return false;
        }
        for (char c : dirs) {
            int[] next = dirToIndex(c, cx, cy);
            if (miro[next[0]][next[1]] == '.' || miro[next[0]][next[1]] == 'e') {
                cnt++;
                if (dfs(next[0], next[1])){
                    result = c + result;
                    return true;
                } 
                cnt--;
            }
        }
        return false;
    }
    
    int[] dirToIndex(char c, int row, int col) {
        if (c == 'd')
            return new int[] {row+1, col};
        if (c == 'l')
            return new int[] {row, col-1};
        if (c == 'r')
            return new int[] {row, col+1};
        if (c == 'u')
            return new int[] {row-1, col};
        
        return null;
    }
}
/*
dfs 쓰려면 가치지기 필요 (아니면 지금처럼 시간초과)
bfs가 더 효율적일듯
*/
