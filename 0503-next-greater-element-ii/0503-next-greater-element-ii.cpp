class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> ans(nums.size(), -1);
        stack<int> s;

        for (int i = 2 * nums.size() - 1; i >= 0; i--) {
            int idx = i % nums.size();

            while (!s.empty() && s.top() <= nums[idx]) {
                s.pop();
            }

            if (i < nums.size()) {
                if (!s.empty()) {
                    ans[idx] = s.top();
                }
            }

            s.push(nums[idx]);
        }

        return ans;
    }
};
