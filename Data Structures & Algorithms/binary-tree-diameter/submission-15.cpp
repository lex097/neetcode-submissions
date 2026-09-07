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
    int diameterOfBinaryTree(TreeNode* root) {
        int ret = 0;
        dfs(root, ret);

        return ret;

    }
    int dfs(TreeNode* node, int& ret) {
        if (node == nullptr) {
            return 0;
        }
        int l = dfs(node->left, ret);
        int r = dfs(node->right, ret);
        ret = max(ret, l + r);

        return 1 + max(l, r);

    }
};
