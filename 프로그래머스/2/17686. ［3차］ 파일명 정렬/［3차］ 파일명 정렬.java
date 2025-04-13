import java.util.*;
import java.util.regex.*;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                Pattern pattern = Pattern.compile("([a-zA-Z\\s-.]+)([0-9]{1,5})");

                Matcher m1 = pattern.matcher(o1);
                Matcher m2 = pattern.matcher(o2);

                if (m1.find() && m2.find()) {
                    String head1 = m1.group(1).toLowerCase();
                    String head2 = m2.group(1).toLowerCase();

                    if (!head1.equals(head2)) {
                        return head1.compareTo(head2);
                    }

                    int num1 = Integer.parseInt(m1.group(2));
                    int num2 = Integer.parseInt(m2.group(2));

                    return Integer.compare(num1, num2);
                }

                return o1.compareTo(o2);
            }
        });

        return files;
    }
}
