import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int bx = Integer.parseInt(st.nextToken());
		int by = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int gx = Integer.parseInt(st.nextToken());
		int gy = Integer.parseInt(st.nextToken());

		int maxx = Math.max(bx, gx);
		int minx = Math.min(bx, gx);
		int maxy = Math.max(by, gy);
		int miny = Math.min(by, gy);

		int count = 0;
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int nx = Integer.parseInt(st.nextToken());
			int ny = Integer.parseInt(st.nextToken());

			if (nx > minx && nx < maxx && ny > miny && ny < maxy) {
				count++;
			}
		}

		String ans = "";
		if ((bx-gx)*(bx-gx) + (by-gy)*(by-gy) >= 25 && count >= 3)
			ans = "YES";
		else
			ans = "NO";
		
		System.out.println(ans);
	}
}
/* 맹수포획: 주어지는 맹수와 사냥꾼 좌표로 덫이 작동하여 맹수가 잡힐지 말지를 판별 */
