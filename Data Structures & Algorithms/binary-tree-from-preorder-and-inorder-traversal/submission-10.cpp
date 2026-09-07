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
    TreeNode* build(unordered_map<int, int>& inorder_map, int l, int r, vector<int>& preorder, vector<int>& inorder, int& idx) {

        if (l > r) {
            return nullptr;
        } else if (l == r) {
            idx++;
            return new TreeNode(inorder[l]);
        }
        int el = preorder[idx];
        TreeNode* node = new TreeNode(preorder[idx]);
        int m = inorder_map[el];
        idx++;
        node->left = build(inorder_map, l, m - 1, preorder, inorder, idx);
        node->right = build(inorder_map, m + 1, r, preorder, inorder, idx);
        return node;

    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inorder_map;
        for (int i = 0; i < inorder.size(); i++) {
            inorder_map[inorder[i]] = i;
        }
        int idx {0};
        return build(inorder_map, 0, preorder.size() - 1, preorder, inorder, idx);
    }
};
