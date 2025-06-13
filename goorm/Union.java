import java.io.*;
import java.util.*;

class Main {
	static ArrayList<Integer>[] G;
	static boolean[] V;
	static int ans;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);

		int island = sc.nextInt();
		int bridge = sc.nextInt();

		G = new ArrayList[island + 1];
		for (int i = 0; i < island + 1; i++) 
			G[i] = new ArrayList<Integer>();

		HashSet<String> oneWay = new HashSet<>();
		for (int i = 0; i < bridge; i++) {
			int s = sc.nextInt();
			int e = sc.nextInt();

			if (oneWay.remove(e + " " + s)) {
				G[s].add(e);
				G[e].add(s);
			} else {
				oneWay.add(s + " " + e);
			}
		}

		V = new boolean[island + 1];
		ans = 0;
		for (int i = 1; i < island + 1; i++) {
			if (!V[i]) {
				ans++;
				dfs(i);
			}
		}
		
		System.out.println(ans);
	}

	static void dfs(int cur) {
		V[cur] = true;
		for (int next : G[cur]) {
			if (!V[next]) 
				dfs(next);
		}
	}
}

/* 연합: 주어지는 단방향 노선 중 양방향이 되는 노드들만 연합을 결성. 연합 수 구하기 - Graph, dfs, HashSet
	-> 양방향이 되는 엣지만 그래프에 포함시키고, 단방향은 포함x(HashSet활용). 이후 서로 연결된 연합수 구하기.
*/
