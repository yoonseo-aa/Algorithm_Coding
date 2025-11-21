class Solution {
    public int[] solution(String[] wallpaper) {
        int lux = wallpaper.length;
        int luy = wallpaper[0].length();
        int rux = 0;
        int ruy = 0;
        
        String[][] map = new String[wallpaper.length][];
        for(int i = 0; i < wallpaper.length; i++){
            map[i] = wallpaper[i].split("");
        }
        
        for(int i = 0; i < wallpaper.length; i++){
            for(int j = 0; j < wallpaper[i].length(); j++){
                if(map[i][j].equals("#")){
                    lux = Math.min(lux, i);
                    luy = Math.min(luy, j);
                    rux = Math.max(rux, i);
                    ruy = Math.max(ruy, j);
                }
            }
        }
        return new int[]{lux, luy, rux + 1, ruy + 1};
    }
}