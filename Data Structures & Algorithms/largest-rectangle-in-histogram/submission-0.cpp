class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;
        int n = heights.size();
        vector<pair<int, int>> stack;  // {start index, height}

        for (int i = 0; i < n; i++) {
            int start = i;
            int height = heights[i];
            while (!stack.empty() && stack.back().second > height) {
                auto [idx, h] = stack.back();
                stack.pop_back();
                maxArea = max(maxArea, h * (i - idx));
                start = idx;
            }
            stack.push_back({start, height});
        }

        for (auto [idx, h] : stack) {
            maxArea = max(maxArea, h * (n - idx));
        }
        return maxArea;
    }
};