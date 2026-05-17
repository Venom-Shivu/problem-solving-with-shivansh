class Solution {
public:

    vector<int> findSubstring(string s, vector<string>& words) {

        vector<int> result;

        int wordLen = words[0].size();
        int wordCount = words.size();

        int totalLen = wordLen * wordCount;

        // Frequency map of required words
        unordered_map<string, int> target;

        for (string word : words) {
            target[word]++;
        }

        // We try all possible starting offsets
        for (int offset = 0; offset < wordLen; offset++) {

            int left = offset;
            int count = 0;

            unordered_map<string, int> window;

            // Move in chunks of word length
            for (int right = offset;
                 right + wordLen <= s.size();
                 right += wordLen) {

                string word = s.substr(right, wordLen);

                // Valid word found
                if (target.count(word)) {

                    window[word]++;
                    count++;

                    // Too many occurrences
                    while (window[word] > target[word]) {

                        string leftWord = s.substr(left, wordLen);

                        window[leftWord]--;
                        left += wordLen;
                        count--;
                    }

                    // Perfect match
                    if (count == wordCount) {

                        result.push_back(left);

                        // Move window forward
                        string leftWord = s.substr(left, wordLen);

                        window[leftWord]--;
                        left += wordLen;
                        count--;
                    }
                }

                else {

                    // Invalid word
                    window.clear();

                    count = 0;

                    left = right + wordLen;
                }
            }
        }

        return result;
    }
};