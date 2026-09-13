class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            int el = nums[i];
            if (ans.size() == 0) {
                ans.push_back(el);
                continue;
            }
            auto it = lower_bound(ans.begin(), ans.end(), el);
            if (it == ans.end()) {
                ans.push_back(el);
            } else {
                ans[it - ans.begin()] = el;
            }
        }
        return ans.size();

    }
};
