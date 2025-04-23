import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] person1 = {1,2,3,4,5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        Map<String, Integer> score = new HashMap<>();
        score.put("1", 0);
        score.put("2", 0);
        score.put("3", 0);
        
        for(int i= 0; i < answers.length; i++){
            if(answers[i] == person1[i%person1.length]) score.put("1", score.get("1")+1);
            if(answers[i] == person2[i%person2.length]) score.put("2", score.get("2")+1);
            if(answers[i] == person3[i%person3.length]) score.put("3", score.get("3")+1);
        }
        
        int maxScore = Collections.max(score.values());
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(String key : score.keySet()){
            if(score.get(key) == maxScore){
                answer.add(Integer.parseInt(key)); 
            }
        }
        
        Collections.sort(answer);
        
        int[] result = new int[answer.size()];
        
        for(int j=0; j < answer.size(); j++){
            result[j] = answer.get(j);
        }
        
        return result;
    }
}