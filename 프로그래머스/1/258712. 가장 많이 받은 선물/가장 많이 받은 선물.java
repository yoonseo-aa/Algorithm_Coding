import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0; i<friends.length; i++) {
            map.put(friends[i], i);
        }

        int[][] giftsArr = new int[friends.length][friends.length];
        int[] giftPoint = new int[friends.length];

        for(int i=0; i<gifts.length; i++) {
            String[] split = gifts[i].split(" ");
            String giver = split[0];
            String taker = split[1];
            int giverIndex = map.get(giver);
            int takerIndex = map.get(taker);

            giftsArr[giverIndex][takerIndex]++;
            giftPoint[giverIndex]++;
            giftPoint[takerIndex]--;
        }

        int[] nextMonthGift = new int[friends.length];

        for(int i=0; i<giftsArr.length; i++) {

            for(int j=i+1; j<giftsArr[i].length; j++) {
                if(giftsArr[i][j] > giftsArr[j][i]) {
                    nextMonthGift[i]++;
                } else if (giftsArr[i][j] < giftsArr[j][i]) {
                    nextMonthGift[j]++;
                } else {
                    if(giftPoint[i] > giftPoint[j]) {
                        nextMonthGift[i]++;
                    } else if (giftPoint[i] < giftPoint[j]) {
                        nextMonthGift[j]++;
                    }

                }

            }
        }
        return Arrays.stream(nextMonthGift).max().getAsInt();
    }
}