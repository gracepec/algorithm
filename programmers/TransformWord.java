import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) { 
        Set<String> visited = new HashSet<>();
        
        Deque<Node> q = new ArrayDeque<>();
        q.add(new Node(begin, 0));
        
        while(!q.isEmpty()) {
            // System.out.println(q);
            Node cur = q.poll();
            
            if (cur.word.equals(target)) 
                return cur.depth;
        
            for (String next : words) {
                if (!visited.contains(next) && isTransform(cur.word, next)) {
                    visited.add(next);
                    q.add(new Node(next, cur.depth+1));
                }
            }
        }
        
        return 0;
    }
    
    boolean isTransform(String A, String B) {
        int cnt = 0;
        for (int i = 0; i < A.length(); i++)
            if (A.charAt(i) != B.charAt(i))
                cnt++;
        
        if (cnt == 1) return true;
        else return false;
    }
    
    class Node {
        String word;
        int depth;
        
        Node(String word, int depth) {
            this.word = word;
            this.depth = depth;
        }
        
        @Override
        public String toString() {
            return "(" + word + ", " + depth + ")";
        }
    }
}
