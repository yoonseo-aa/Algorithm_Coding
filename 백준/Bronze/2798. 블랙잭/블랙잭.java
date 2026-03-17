import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str1 = br.readLine().split(" ");
        String[] str2 = br.readLine().split(" ");
        int n = Integer.parseInt(str1[0]);
        int m = Integer.parseInt(str1[1]);

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(str2[i]);
        }

        int maxSum = 0;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int sum = arr[i] + arr[j] + arr[k];
                    if (sum <= m) {
                        maxSum = Math.max(maxSum, sum);
                    }
                }
            }
        }

        System.out.println(maxSum);
    }
}
