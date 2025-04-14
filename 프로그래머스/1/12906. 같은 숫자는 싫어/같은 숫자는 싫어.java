import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        Deque<Integer> deque = new ArrayDeque<>();

        for (int num : arr) {
            if (deque.isEmpty() || deque.peekLast() != num) {
                deque.addLast(num);
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
