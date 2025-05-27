import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            int N = Integer.parseInt(line);

            Char[] C = new Char[3**N];
            
            Cantor(C)
        }
    }

    private void Cantor(String[] C, int l, int r) {
        tri = (r-l+1) / 3;

        for (int i = 0; i < tri; i++)
            C[l+tri+i] = ' ';
        
        if (tri > 1) {
            for (int i = l; i < r; i++)
                System.out.print(C[i])
            return;
        }
        
        Cantor(C, l, l+tri);
        Cantor(C, l+tri*2, r);

    }
}
