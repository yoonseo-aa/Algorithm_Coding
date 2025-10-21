class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        int product = 1;
        
        for (int n : num_list) {
            sum += n;
            product *= n;
        }
        
        if (product < sum * sum) {
            return 1;
        } else {
            return 0;
        }
    }
}
