class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        
        int n = arr.size();

        // To avoid visiting same index multiple times
        vector<bool> visited(n, false);

        queue<int> q;

        q.push(start);
        visited[start] = true;

        while (!q.empty()) {

            int idx = q.front();
            q.pop();

            // If we reach value 0
            if (arr[idx] == 0)
                return true;

            // Forward jump
            int forward = idx + arr[idx];

            // Backward jump
            int backward = idx - arr[idx];

            // Check forward index
            if (forward < n && !visited[forward]) {
                visited[forward] = true;
                q.push(forward);
            }

            // Check backward index
            if (backward >= 0 && !visited[backward]) {
                visited[backward] = true;
                q.push(backward);
            }
        }

        return false;
    }
};