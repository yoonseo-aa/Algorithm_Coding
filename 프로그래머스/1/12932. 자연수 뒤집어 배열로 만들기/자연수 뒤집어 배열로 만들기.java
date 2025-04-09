import java.util.*;

class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        int[] result = new int[str.length()];

        for (int i = 0; i < str.length(); i++) {
            result[i] = str.charAt(str.length() - 1 - i) - '0';
        }

        return result;
    }
}
