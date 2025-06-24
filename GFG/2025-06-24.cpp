class Solution {
public:
    string maxSubseq(string& s, int k) {
        int n = s.size();
        int keep = n - k;
        string stack;

        for (char ch : s) {
            while (!stack.empty() && k > 0 && stack.back() < ch) {
                stack.pop_back();
                k--;
            }
            stack.push_back(ch);
        }

        return stack.substr(0, keep);
    }
};
