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
		
		for (int i = 0; i < bridge; i++) {
			int s = sc.nextInt();
			int e = sc.nextInt();
			G[s].add(e);
		}

		V = new boolean[island + 1];
		ans = island;
		for (int i = 1; i < island + 1; i++)
			run(i);
		
		System.out.println(ans);
	}

	static void run(int cur) {
		for (int next : G[cur]) {
			if (G[next].remove(new Integer(cur))) {
				ans--;
			}
		}
	}
}

/* 연합: 주어지는 단방향 노선 중 양방향이 되는 노드들만 연합을 결성. 연합 수 구하기 - Graph, dfs, HashSet 혹은 Map
	-> 양방향이 되는 엣지만 그래프에 포함시키고, 단방향은 포함x(set). 이후 서로 연결된 연합수 구하기.
*/
