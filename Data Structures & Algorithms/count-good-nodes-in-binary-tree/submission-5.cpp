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
    void dfs(TreeNode* node, int& ret, int mx) {
        mx = max(mx, node->val);
        // cout << node->val << " " << mx << endl;
        if (node->left != nullptr) {
            if (node->left->val >= mx) {
                ret++;
            }
            dfs(node->left, ret, mx);
        }
        if (node->right != nullptr) {
            if (node->right->val >= mx) {
                ret++;
            }
            dfs(node->right, ret, mx);
        }
        
    }
    int goodNodes(TreeNode* root) {
        int ret {1};
        dfs(root, ret, INT_MIN);
        return ret;
    }
};
