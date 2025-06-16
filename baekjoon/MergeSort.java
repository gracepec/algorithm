import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }

        merge_sort(A, 0, n-1);

        System.out.println(Arrays.toString(A));
    }

    // # A[p..r]을 오름차순 정렬한다.
    static void merge_sort(int[] A, int p, int r) {
        if (p < r) {
            int q = (int) Math.ceil((p + r) / 2); // # q는 p, r의 중간 지점
            merge_sort(A, p, q);                  // # 전반부 정렬
            merge_sort(A, q + 1, r);              // # 후반부 정렬
            merge(A, p, q, r);                    // # 병합
        }
    }
    
    // # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
    // # A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
    static void merge(int[] A, int p, int q, int r) {
        int i = p;
        int j = q + 1;
        int t = 1;

        int[] tmp = new int[A.length + 1];
        while (i <= q && j <= r) {
            if (A[i] <= A[j])
                tmp[t++] = A[i++];  // # tmp[t] <- A[i]; t++; i++;
            else
                tmp[t++] = A[j++];  // # tmp[t] <- A[j]; t++; j++;
        }
        while (i <= q) // # 왼쪽 배열 부분이 남은 경우
            tmp[t++] = A[i++];
        while (j <= r) // # 오른쪽 배열 부분이 남은 경우
            tmp[t++] = A[j++];
        i = p;
        t = 1;
        while (i <= r) // # 결과를 A[p..r]에 저장
            A[i++] = tmp[t++];
    }
}
/* 24060
알고리즘 수업 - 병합 정렬 1: 주어진 수도코드로 병합정렬이 이루어지는 k번째 수 찾기
    -> 아직 여기까지 코드는 그냥 받은 배열 병합 정렬하는 거 까지만 구현,
*/
