class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> tmp;
        int tmp_i;

        
        tmp.push_back(nums[0]);
        tmp_i = nums[0];

        for(int i=1; i<nums.size(); i++) {
            if(tmp_i != nums[i]) {
                tmp.push_back(nums[i]);
                tmp_i = nums[i];
            } else {
                continue;
            }
        }

        nums = tmp;
        return tmp.size();
        
    }
};