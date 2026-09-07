class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> freq;
        unordered_set<int> used;
        for (int num : arr1) {
            freq[num]++;
        }
        vector<int> ret;

        for (int num : arr2) {
            for (int i = 0; i < freq[num]; i++) {
                ret.push_back(num);
                used.insert(num);
            }
        }
        vector<int> notUsed;
        for (const auto& [k, v] : freq) {
            if (!used.count(k)) {
                notUsed.push_back(k);
            }
        }
        sort(notUsed.begin(), notUsed.end());
        for (int num : notUsed) {
            for (int i = 0; i < freq[num]; i++) {
                ret.push_back(num);
            }

        }
        return ret;
    }
};