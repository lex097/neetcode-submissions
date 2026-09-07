class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<long long> dp(amount + 1, INT_MAX);
        // cout << dp[1] << endl;
        dp[0] = 0;

        for (long long i = 0; i <= amount; i++) {
            if (dp[i] == INT_MAX) {
                continue;
            }
            for (const auto& coin : coins) {
                if (i + coin <= amount) {
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin]);
                }
            }
        }

        if (dp[amount] == INT_MAX) {
            return -1;
        } else {
            return dp[amount];
        }

    }
};
