import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String head = o1.split("[0-9]")[0].toLowerCase();
                String number = o2.split("[0-9]")[0].toLowerCase();

                if (!head.equals(number)) {
                    return head.compareTo(number);
                }

                String num1Str = o1.substring(head.length());
                String num2Str = o2.substring(number.length());

                num1Str = getLeadingNumber(num1Str);
                num2Str = getLeadingNumber(num2Str);

                int num1 = Integer.parseInt(num1Str);
                int num2 = Integer.parseInt(num2Str);

                return Integer.compare(num1, num2);
            }

            private String getLeadingNumber(String str) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < str.length(); i++) {
                    if (Character.isDigit(str.charAt(i)) && sb.length() < 5) {
                        sb.append(str.charAt(i));
                    } else {
                        break;
                    }
                }
                return sb.toString();
            }
        });

        return files;
    }
}
