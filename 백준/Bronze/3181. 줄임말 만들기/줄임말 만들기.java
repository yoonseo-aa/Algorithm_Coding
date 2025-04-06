import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        String[] tmp = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"};
        List<String> tmpList = new ArrayList<>(Arrays.asList(tmp));

        String[] words = str.split(" ");
        List<String> strList = new ArrayList<>(Arrays.asList(words));

        int i = 0;
        for (String s : strList) {
            if (i == 0 || !tmpList.contains(s)) {
                System.out.print(Character.toUpperCase(s.charAt(0))); 
            }
            i++;
        }
    }
}
