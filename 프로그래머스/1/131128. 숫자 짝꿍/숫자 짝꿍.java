class Solution {
    public String solution(String X, String Y) {
        int[] cntX = new int[10];
        int[] cntY = new int[10];

        for (int i = 0; i < X.length(); i++) cntX[X.charAt(i) - '0']++;
        for (int i = 0; i < Y.length(); i++) cntY[Y.charAt(i) - '0']++;

        StringBuilder sb = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            int common = Math.min(cntX[d], cntY[d]);
            for (int k = 0; k < common; k++) sb.append(d);
        }

        if (sb.length() == 0) return "-1";      // 공통 숫자 없음
        if (sb.charAt(0) == '0') return "0";    // 0으로만 구성
        return sb.toString();
    }
}