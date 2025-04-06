import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();  // 입력 받기 (예: "i am a student and i love java")

        String[] tmp = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"};
        List<String> tmpList = new ArrayList<>(Arrays.asList(tmp));

        String[] words = str.split(" "); // 문자열을 단어 단위로 나누기
        List<String> strList = new ArrayList<>(Arrays.asList(words));

        int i = 0;
        for (String s : strList) {
            if (i == 0 || !tmpList.contains(s)) {
                System.out.print(Character.toUpperCase(s.charAt(0)));  // 한 글자만 대문자로 출력
            }
            i++;
        }
    }
}
