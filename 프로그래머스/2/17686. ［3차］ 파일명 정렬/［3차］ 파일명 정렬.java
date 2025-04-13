import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String head1 = o1.split("[0-9]")[0].toLowerCase();
                String head2 = o2.split("[0-9]")[0].toLowerCase();

                if (!head1.equals(head2)) {
                    return head1.compareTo(head2);
                }

                int number1 = Integer.parseInt(getNumber(o1, head1.length()));
                int number2 = Integer.parseInt(getNumber(o2, head2.length()));

                return Integer.compare(number1, number2);
            }

            private String getNumber(String file, int index) {
                StringBuilder number = new StringBuilder();
                for (int i = index; i < file.length(); i++) {
                    char ch = file.charAt(i);
                    if (Character.isDigit(ch) && number.length() < 5) {
                        number.append(ch);
                    } else {
                        break;
                    }
                }
                return number.toString();
            }
        });

        return files;
    }
}
