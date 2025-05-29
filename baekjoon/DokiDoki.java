import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Deque<Integer> wait = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            wait.add(Integer.parseInt(st.nextToken()));

        Deque<Integer> shelter = new ArrayDeque<>();

        int turn = 1;
        while (!wait.isEmpty()) {
            int p = wait.poll();
            if (p == turn) 
                turn++;
            else 
                shelter.push(p);

            while (!shelter.isEmpty()) {
                if (shelter.peek() == turn) {
                    shelter.poll();
                    turn++;
                } else break;
            }
        }

        if (wait.isEmpty() && shelter.isEmpty())
            System.out.println("Nice");
        else
            System.out.println("Sad");
    }
}

/* 12789
# 도키도키 간식드리미: T자 길에서 순서대로 간식받기 - Queue, Stack
*/
