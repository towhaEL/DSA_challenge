class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j,k;

        if(nums.size()==0) {
            return 0;
        }else {
            for(int i=nums.size()-1; i>=0; i--) {
                if(nums[i]!=val) {
                    k = i;
                    j = i-1;
                    break;
                }
            }

            for(; j>=0; j--) {
                if(nums[j] == val) {
                    swap(nums[j], nums[k]);
                    k--;
                }
            }

            return nums.size() - count(nums.begin(), nums.end(), val);
            
        }
    }
};