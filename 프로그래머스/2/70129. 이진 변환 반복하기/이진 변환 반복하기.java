class Solution {
    public int[] solution(String s) {
        
        int countTrasform = 0;
        int countRemovedZero = 0;
        
        while(!s.equals("1")){
            
            int lengthBefore = s.length(); 
            s = s.replace("0","");
            int lengthAfter = s.length(); 
            
            countRemovedZero += (lengthBefore - lengthAfter);
            s = Integer.toBinaryString(lengthAfter); 
            countTrasform++; 
            
        }
        
        return new int[] {countTrasform, countRemovedZero};
    }
}