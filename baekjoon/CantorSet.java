import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            int N = Integer.parseInt(line);
            int p = (int) Math.pow(3, N);
            
            char[] C = new char[p];
            Arrays.fill(C, '-');
            
            Cantor(C, 0, p);
            System.out.println(C);
        }
    }

    private static void Cantor(char[] C, int l, int r) {
        int tri = (r-l+1) / 3;

        for (int i = 0; i < tri; i++)
            C[l+tri+i] = ' ';
        
        if (tri > 1) {
            Cantor(C, l, l+tri);
            Cantor(C, l+tri*2, r);
        }
    }
}
