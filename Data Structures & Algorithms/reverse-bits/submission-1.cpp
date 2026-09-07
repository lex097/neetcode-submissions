using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ret {0};
        uint32_t curr = 1 << 31;
        cout << curr << endl;
        for (int i = 0; i < 32; i++) {
            if (n % 2 == 1) {
                ret += curr;
                cout << ret << endl;
            }
            curr = curr >> 1;
            n = n >> 1;
        }
        return ret;
    }
};
