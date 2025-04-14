import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        Deque<Integer> deque = new ArrayDeque<>();

        Integer prev = null;
        for (int num : arr) {
            if (prev == null || prev != num) {
                deque.add(num);
                prev = num;
            }
        }
        
        int[] answer = new int[deque.size()];
        int i = 0;
        for (int num : deque) {
            answer[i++] = num;
        }

        return answer;
    }
}
