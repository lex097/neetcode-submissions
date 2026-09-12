class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int ret {0};

        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size(), 0));


        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == '0') {
                    continue;
                }
                int left {0}; int up {0}; int diag {0};
                if (i > 0) {
                    left = dp[i - 1][j];
                }
                if (j > 0) {
                    up = dp[i][j - 1];
                }
                if (i > 0 and j > 0) {
                    diag = dp[i - 1][j - 1];
                }

                dp[i][j] = min(left + 1, min(up + 1, diag + 1));

                ret = max(ret, dp[i][j]);

            }
        }

        return ret * ret;

    }
};