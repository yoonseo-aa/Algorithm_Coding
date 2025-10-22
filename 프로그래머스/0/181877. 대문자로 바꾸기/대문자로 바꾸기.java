class Solution {
    public String solution(String myString) {
        StringBuffer answer = new StringBuffer();
        int s_len = myString.length();
        char[] arr = new char[s_len];
        for(int i=0; i < s_len; i++){
          arr[i] = myString.charAt(i);
        }
        for(int j = 0; j < arr.length; j++){
            if(Character.isLowerCase(arr[j])){
                answer.append(Character.toUpperCase(arr[j]));
            }else{
                answer.append(arr[j]);
            }
        }
        return answer.toString();
    }
}