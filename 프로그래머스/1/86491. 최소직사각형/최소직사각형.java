class Solution {
    public int solution(int[][] sizes) {
        int xMax = 0;
        int hMax = 0;
        for(int i=0; i < sizes.length; i++){
            xMax = Math.max(xMax,Math.max(sizes[i][0],sizes[i][1]));
            hMax = Math.max(hMax,Math.min(sizes[i][0],sizes[i][1]));
        }
        
        return xMax*hMax;
    }
}