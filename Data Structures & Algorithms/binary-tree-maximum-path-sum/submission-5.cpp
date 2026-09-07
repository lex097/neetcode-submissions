/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int dfs(TreeNode* node, int& ret) {

        if (node->left == nullptr and node->right == nullptr) {
            // cout << max(node->val, 0) << endl;
            ret = max(ret, node->val);
            return max(node->val, 0);
        }
        int left {0};
        int right {0};
        if (node->left != nullptr) {
            left = dfs(node->left, ret);
        }
        if (node->right != nullptr) {
            right = dfs(node->right, ret);
        }
        // cout << node->val << " " << left << " " << right << endl;
        ret = max(ret, left + right + node->val);
        return max(left + node->val, max(right + node->val, 0));

    }
    int maxPathSum(TreeNode* root) {
        int ret {root->val};
        dfs(root, ret);
        return ret;
    }
};
