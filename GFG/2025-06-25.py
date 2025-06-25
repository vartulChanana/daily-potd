#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool sameFreq(string& s) {
        unordered_map<char, int> charCount;
        for (char c : s) {
            charCount[c]++;
        }

        unordered_map<int, int> freqCount;
        for (const auto& entry : charCount) {
            freqCount[entry.second]++;
        }

        if (freqCount.size() == 1) {
            return true;
        }

        if (freqCount.size() > 2) {
            return false;
        }

        auto it = freqCount.begin();
        int freq1 = it->first;
        int count1 = it->second;
        it++;
