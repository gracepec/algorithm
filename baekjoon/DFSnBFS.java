import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int edge = sc.nextInt();
        int sn = sc.nextInt();

        for (int i = 0; i < edge; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
        }
        
        System.out.println(n);
    }
}

/* 빠른 입력처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int edge = Integer.parseInt(st.nextToken());
        int sn = Integer.parseInt(st.nextToken());

        
        for (int i = 0; i < edge; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
        }
*/
