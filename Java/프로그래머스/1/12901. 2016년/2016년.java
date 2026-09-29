class Solution {
    public String solution(int a, int b) {
        int[] days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] week = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        
        
        int total = b-1;
        for(int i=0; i < a-1; i++){
            total += days[i];
        }
        
        return week[total%7];
    }
}