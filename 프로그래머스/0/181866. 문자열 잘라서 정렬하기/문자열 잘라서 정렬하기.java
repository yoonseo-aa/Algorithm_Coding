import java.util.*;

class Solution {
    public String[] solution(String myString) {
        List<String> answer = new ArrayList<>();
        int start = 0;
        int index;

        while ((index = myString.indexOf("x", start)) != -1) {
            answer.add(myString.substring(start, index));
            start = index + 1;
        }
        answer.add(myString.substring(start));
        answer.removeIf(String::isEmpty);
        Collections.sort(answer);

        return answer.toArray(new String[0]);
    }
}
