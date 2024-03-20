class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        pair<int, int> curr_count(nums[len-1], 0);

        for(int i=len-1; i>=0; i--) {
            if(nums[i] == curr_count.first) {
                curr_count.second++;
            } else {
                curr_count.first = nums[i];
                curr_count.second = 1;
            }

            if(curr_count.second <= 2) {
                nums.push_back(nums[i]);
            } else {
                continue;
            }        
        }

        reverse(nums.begin(), nums.end());

        return nums.size() - len;
    }
};