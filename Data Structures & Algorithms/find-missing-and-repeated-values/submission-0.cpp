using namespace std;
class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        vector<int> ret(2);
        unordered_set<int> used;
        for (int i = 0; i < grid.size(); i++) {
            for (int k = 0; k < grid.size(); k++) {
                if (used.count(grid[i][k])) {
                    ret[0] = grid[i][k];
                }
                used.insert(grid[i][k]);
            }
        }
        for (int i = 1; i <= grid.size() * grid.size(); i++) {
            if (!used.count(i)) {
                ret[1] = i;
                break;
            }
        }
        return ret;

    }
};