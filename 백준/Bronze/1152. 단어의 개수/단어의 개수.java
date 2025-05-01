import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().trim();

        if (input.isEmpty()) {
            System.out.println(0); // 공백만 입력한 경우
        } else {
            String[] arr = input.split("\\s+");
            System.out.println(arr.length);
        }
    }
}
