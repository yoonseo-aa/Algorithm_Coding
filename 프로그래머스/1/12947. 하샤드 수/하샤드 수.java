class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        String strNum = Integer.toString(x);
        int[] arrNum = new int[strNum.length()];
        for (int i = 0; i < strNum.length(); i++) {
            arrNum[i] = strNum.charAt(i) - '0';
        }
        for(int j = 0; j < arrNum.length; j++){
            sum += arrNum[j];
        }
        if(x%sum != 0){
            answer = false;
        }
        return answer;
    }
}