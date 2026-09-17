class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {

        unordered_map<int, int> dp;
        dp[0] = 1;
        for (int num : nums) {
            unordered_map<int, int> nw;
            for (const auto [k, v] : dp) {
                nw[k + num] += v;
                nw[k - num] += v;
            }
            dp = nw;
        }
        return dp[target];

    }
};
