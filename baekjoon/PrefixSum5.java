import java.util.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[][] N = new int[n+1][n+1];
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                N[i][j] = sc.nextInt();
            }
        }

        int[][] M = new int[m][4];
        for (int i = 0; i < m; i++){
            for (int j = 0; j < 4; j++){
                M[i][j] = sc.nextInt();
            }
        }

        int[][] dp = new int[n+1][n+1];
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                            - dp[i-1][j-1] + N[i][j];
            }
        }

        for (int i = 0; i < m; i++) {
            int x1 = M[i][0], y1 = M[i][1],
                x2 = M[i][2], y2 = M[i][3];
            int ans = dp[x2][y2] - dp[x1-1][y2]
                        -dp[x2][y1-1] + dp[x1-1][y1-1];
            System.out.println(ans);
        }
    }
}

/* 11660
# 2차원 누적 합 - DP, prefix sum

    """ 행별로 누적합 - 가능하지만 시간초과

        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][0] = N[i][0];
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i][j-1] + N[i][j];
            }
        }
        // System.out.println(Arrays.deepToString(dp));

        for (int i = 0; i < m; i++) {
            int ans = 0;
            for (int j = M[i][0]; j <= M[i][2]; j++) {
                if (M[i][1] == 0) ans += dp[j][M[i][3]];
                else ans += dp[j][M[i][3]] - dp[j][M[i][1]-1];
            }
            System.out.println(ans);
        }
    """
*/
