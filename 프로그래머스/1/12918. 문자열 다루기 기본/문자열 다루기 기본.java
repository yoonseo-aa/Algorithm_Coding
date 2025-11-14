class Solution {
    public boolean solution(String s) {
        if (s == null) return false;
        if (s.length() != 4 && s.length() != 6) return false;

        for (char c : s.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false;
            }
        }
        return true;
    }
}