class Solution {
    public int solution(int a, int b) {
        String strA = String.valueOf(a);
        String strB = String.valueOf(b);

        int num1 = Integer.parseInt(strA + strB);
        int num2 = Integer.parseInt(strB + strA);

        return Math.max(num1, num2);
    }
}