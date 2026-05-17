class Solution {

    public String countAndSay(int n) {

        // Base sequence
        String result = "1";

        // Generate sequence from 2 to n
        for (int i = 2; i <= n; i++) {

            StringBuilder next = new StringBuilder();

            int count = 1;

            // Traverse current result
            for (int j = 1; j < result.length(); j++) {

                // Same digit continues
                if (result.charAt(j) == result.charAt(j - 1)) {

                    count++;
                }

                else {

                    // Append count + digit
                    next.append(count);
                    next.append(result.charAt(j - 1));

                    // Reset count
                    count = 1;
                }
            }

            // Append last group
            next.append(count);
            next.append(result.charAt(result.length() - 1));

            // Update result
            result = next.toString();
        }

        return result;
    }
}