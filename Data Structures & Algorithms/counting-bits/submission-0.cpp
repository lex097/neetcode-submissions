class Solution {
public:
    vector<int> countBits(int n) {
        // dp[n] -> # of 1s,
        // if n & 1 = 0 -> dp[n] = dp[n - 1] + 1
        // 
        vector<int> dp(n + 1);
        int offset = 1;
        for (int i = 1; i <= n; i++) {
            if (offset * 2 == i) {
                offset = i;
            }
            dp[i] = 1 + dp[i - offset];
        }

        return dp;
    }
};
