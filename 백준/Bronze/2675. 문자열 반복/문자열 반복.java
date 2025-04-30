import java.io.*;

public class Main {
     public static void main(String[] args) throws IOException {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
         int t = Integer.parseInt(br.readLine());  // 테스트케이스 개수
         
         for (int k = 0; k < t; k++) {
             String[] str = br.readLine().split(" ");
             int r = Integer.parseInt(str[0]);
             StringBuilder answer = new StringBuilder();

             for (int i = 0; i < str[1].length(); i++) {
                 for (int j = 0; j < r; j++) {
                     answer.append(str[1].charAt(i));  // 문자 r번 반복
                 }
             }

             System.out.println(answer);
         }
     }
}
