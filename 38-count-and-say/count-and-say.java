class Solution {

    public String countAndSay(int n) {

        String current = "1";

        for (int i = 2; i <= n; i++) {

            char[] arr = current.toCharArray();

            StringBuilder next = new StringBuilder();

            int count = 1;

            for (int j = 1; j < arr.length; j++) {

                if (arr[j] == arr[j - 1]) {

                    count++;
                }

                else {

                    next.append(count);
                    next.append(arr[j - 1]);

                    count = 1;
                }
            }

            // Append last group
            next.append(count);
            next.append(arr[arr.length - 1]);

            current = next.toString();
        }

        return current;
    }
}