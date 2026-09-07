/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<pair<int, int>> times; // time -> 0 is end 1 is start, process ends first

        for (int i = 0; i < intervals.size(); i++) {
            times.push_back({intervals[i].start, 1});
            times.push_back({intervals[i].end, 0});
        }
        sort(times.begin(), times.end(), [](const auto& a, const auto& b){
            if (a.first == b.first) {
                return a.second < b.second;
            } else {
                return a.first < b.first;
            }
        });
        int curr {0};
        int ret {0};
        for (int i = 0; i < times.size(); i++) {
            auto [time, type] = times[i];
            // cout << time << " " << type << endl;

            if (type == 0) {
                curr--;
            } else {
                curr++;
            }
            ret = max(ret, curr);

        }
        return ret;
    }
};
