class Solution {
public:
    int findMin(vector<int> &nums) {
        int L = 0;
        int R = nums.size() - 1;
        while (L < R) {
            int m = (L + R) / 2;
            cout << m << endl;
            if (R - L == 1) {
                return min(nums[R], nums[L]);
            }
            if (nums[R] < nums[L] and nums[m] > nums[L]) {
                L = m + 1;
            } else {
                R = m;
            }


        }
        return nums[L];
    }
};
