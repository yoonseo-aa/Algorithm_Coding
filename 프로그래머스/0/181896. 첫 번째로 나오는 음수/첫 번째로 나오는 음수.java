class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for(int i = 0; i < num_list.length; i++){
            if(num_list[i] < 0 ){
                answer = i;
                break;
            }
        }
        if(answer == 0 && num_list[0] > 0){
            answer = -1;
        }
        return answer;
    }
}