import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringBuilder result = new StringBuilder();
        StringBuilder temp = new StringBuilder();

        boolean isTag = false;

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch == '<') {
                // 단어를 뒤집어서 결과에 추가
                result.append(temp.reverse());
                temp.setLength(0); // 초기화
                isTag = true;
                result.append(ch); // '<' 추가
            } else if (ch == '>') {
                isTag = false;
                result.append(ch); // '>' 추가
            } else if (isTag) {
                result.append(ch); // 태그 내부 문자 그대로 추가
            } else {
                if (ch == ' ') {
                    result.append(temp.reverse()); // 단어 뒤집기
                    result.append(' ');
                    temp.setLength(0); // 초기화
                } else {
                    temp.append(ch); // 단어 만들기
                }
            }
        }

        // 마지막 단어 처리
        result.append(temp.reverse());

        System.out.println(result);
    }
}
