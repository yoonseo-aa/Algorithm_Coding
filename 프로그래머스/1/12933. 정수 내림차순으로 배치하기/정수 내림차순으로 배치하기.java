import java.util.*;

class Solution {
    public long solution(long n) {
        String str = Long.toString(n);
        
        List<String> list = new ArrayList<>();
        
        for(int i =0; i < str.length(); i++){
            list.add(String.valueOf(str.charAt(i)));
        }
        list.sort(Collections.reverseOrder());
        
        StringBuilder answer = new StringBuilder();
        for(int j=0; j < list.size() ; j++){
            answer.append(list.get(j));
        }
        return Long.parseLong(answer.toString());
    }
}