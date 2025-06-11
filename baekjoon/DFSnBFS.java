import java.util.*;
import java.io.*;

class Main {
    static boolean[] V;
    static ArrayList<Integer>[] G;
        
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int edge = sc.nextInt();
        int sn = sc.nextInt();

        // @SuppressWarnings("unchecked")
        G = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) G[i] = new ArrayList<>();

        for (int i = 0; i < edge; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            G[a].add(b);
            G[b].add(a);
        }

        for (int i = 0; i < n+1; i++) Collections.sort(G[i]);

        V = new boolean[n+1];
        dfs(sn);

        System.out.println();
        
        Arrays.fill(V, false);
        bfs(sn);
    }

    static void dfs(int cn) {
        V[cn] = true;
        System.out.print(cn + " ");
        for (int nn : G[cn]) {
            if (!V[nn]) dfs(nn);
        }
    }

    static void bfs(int sn) {
        Deque<Integer> Q = new ArrayDeque<>();
        V[sn] = true;
        Q.add(sn); 
        
        while (!Q.isEmpty()) {
            int cn = Q.poll();
            System.out.print(cn + " ");
            
            for (int nn : G[cn]) {
                if (!V[nn]) {
                    V[nn] = true;
                    Q.add(nn);
                }
            }
        }
    }
}

/* 빠른 입력처리 
            throws IOException
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
