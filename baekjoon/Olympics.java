import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[][] P = new int[n][4];
        for (int i = 0; i < n; i++) {
            P[i][0] = sc.nextInt();
            P[i][1] = sc.nextInt();
            P[i][2] = sc.nextInt();
            P[i][3] = sc.nextInt();            
        }

        Arrays.sort(P, (a,b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            if (a[2] != b[2]) return Integer.compare(a[2], b[2]);
            return Integer.compare(a[3], b[3]);
        });
        // System.out.println(Arrays.deepToString(P));

        int cnt = 0;
        for (int i = 0;;i++) {
            if (P[i][0] == k) {
                for (int j = i+1; j < n; j++) {
                    if (isEqualsMedal(P[j], P[i])) cnt++;
                    else break;
                }
                
                System.out.println(n-i-cnt);
                break;
            }
        }
    }

    private static boolean isEqualsMedal(int[] a, int[] b) {
        return a[1] == b[1] && a[2] == b[2] && a[3] == b[3];
    }
}

/* 8979
# 올림픽 매달 순위 출력 - sort
*/
