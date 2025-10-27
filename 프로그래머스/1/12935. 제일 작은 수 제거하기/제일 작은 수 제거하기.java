class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) return new int[]{-1};
        
        int min_num = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min_num) {
                min_num = arr[i];
            }
        }
        
        int[] answer = new int[arr.length - 1];
        int index = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != min_num) {
                answer[index++] = arr[i];
            }
        }
        
        return answer;
    }
}
