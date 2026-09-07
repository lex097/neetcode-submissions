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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        queue<TreeNode*> q;

        q.push(root);
        vector<vector<int>> ret;
        // cout << q.size() << endl;
        while (q.size() != 0) {
            vector<int> level;
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                // cout << "1";
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left != nullptr) {
                    q.push(node->left);
                }
                if (node->right != nullptr) {
                    q.push(node->right);
                }

            }
            // cout << endl;
            ret.push_back(level);
        }
        return ret;
    }

};
