class Solution {
    public String solution(String str) {
        String answer = "";
        String[] parts = str.split(" ");
        int[] arr = new int[parts.length];
        int i = 0;
        for(String s : str.split(" ")){            
            arr[i++] = Integer.parseInt(s);
        }
        int num_min = arr[0];
        int num_max = arr[0];
        for(int j =0; j < arr.length;j++){
            if(num_max < arr[j]){
                num_max = arr[j];
            }
            if(num_min > arr[j]){
                num_min = arr[j];
            }
            
        }
        answer = num_min + " " + num_max;
        return answer;
    }
}