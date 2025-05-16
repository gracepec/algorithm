import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> wait = new ArrayDeque<>();
        for (int t : truck_weights) wait.add(t);
        
        Deque<Integer> brid = new ArrayDeque<>();
        for (int i = 0; i < bridge_length; i++) brid.add(0);
        
        int time = 0;
        while (wait.size() > 0) {
            time++;
            brid.poll();
            
            int sum = brid.stream().mapToInt(Integer::intValue).sum();
            if (sum + wait.peek() <= weight) brid.add(wait.poll());
            else brid.add(0);
        }
        
        return time + bridge_length;
    }
}

/* 42583
# 다리를 지나는 트럭 - queue

 -> Queue<Integer> q = new ArrayDeque<>();로도 가능 : 기능보장(제한), 성능효율
    q.offer(e), poll, peek 사용
*/
