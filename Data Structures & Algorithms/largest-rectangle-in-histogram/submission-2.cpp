class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n);
        vector<int> right(n);

        vector<int> stack;
        for (int i = 0; i < n; i++) {
            int el = heights[i];
            while (stack.size() > 0 and heights[stack[stack.size() - 1]] >= el) {
                stack.pop_back();
            }

            if (stack.size() == 0) {
                left[i] = -1;
            } else {
                left[i] = stack[stack.size() - 1];
            }

            stack.push_back(i);
        }

        // for (int i = 0 ; i < left.size(); i++) {
        //     cout << i << " " << left[i] << endl;
        // }
        vector<int> stack2;
        for (int i = n - 1; i >= 0; i--) {
            int el = heights[i];
            while (stack2.size() > 0 and heights[stack2[stack2.size() - 1]] >= el) {
                stack2.pop_back();
            }

            if (stack2.size() == 0) {
                right[i] = n;
            } else {
                right[i] = stack2[stack2.size() - 1];
            }

            stack2.push_back(i);
        }
        // for (int i = 0 ; i < left.size(); i++) {
        //     cout << i << " " << right[i] << endl;
        // }
        int ret {INT_MIN};
        for (int i = 0; i < n; i++) {
            int ans = heights[i] * (right[i] - left[i] - 1);
            ret = max(ret, ans);
        }
        return ret;

    }
};
