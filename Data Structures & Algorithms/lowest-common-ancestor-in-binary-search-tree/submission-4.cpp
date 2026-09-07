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
    TreeNode* dfs(TreeNode* node, int p, int q) {
        if (node->val >= p and node->val <= q) {
            return node;
        }

        if (node->val > p and node->val > q) {
            return dfs(node->left, p, q);
        } else {
            return dfs(node->right, p, q);
        }


    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return dfs(root, min(p->val, q->val), max(p->val, q->val));
    }
};
