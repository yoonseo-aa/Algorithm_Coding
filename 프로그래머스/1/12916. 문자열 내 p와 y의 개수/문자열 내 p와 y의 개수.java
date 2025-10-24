class Solution {
    boolean solution(String str) {
        boolean answer = true;
        int s_len = str.length();
        int p_num = 0;
        int y_num = 0;
        int j = 0;
        String arr[] = new String[s_len];
        for(String s : str.split("")){
            if(s.equalsIgnoreCase("p")){
                p_num += 1;
            }
            if(s.equalsIgnoreCase("y")){
                y_num += 1;
            }
        }    
        

        if(p_num != y_num){
            answer = false;
        }
        return answer;
    }
}