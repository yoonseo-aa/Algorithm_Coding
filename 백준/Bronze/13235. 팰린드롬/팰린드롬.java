import java.io.*;
    
public class Main{
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String str = br.readLine();
            String reverseStr = new StringBuilder(str).reverse().toString();
            System.out.println(str.equals(reverseStr));
        }
    }