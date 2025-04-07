import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i = 0; i < commands.length; i++){
            int start = commands[i][0]-1;
            int finish = commands[i][1];
            int k = commands[i][2] -1;
            int[] result = Arrays.copyOfRange(array, start,finish);
            Arrays.sort(result);
            answer[i] = result[k];
        }
        return answer;
    }
}