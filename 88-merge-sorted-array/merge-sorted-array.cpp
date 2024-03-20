class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> tmp;
        int tmp_m = m;
        int tmp_n = n;
        int j=0;
        int k=0;

        
        for(int i=0;i<m+n;i++) {

            if(tmp_m==0) {
                tmp.push_back(nums2[k]);
                k++;
                tmp_n--;
            }else if(tmp_n==0) {
                tmp.push_back(nums1[j]);
                j++;
                tmp_m--;
            }else {
                if(nums1[j] < nums2[k] && tmp_m > 0) {
                    tmp.push_back(nums1[j]);
                    j++;
                    tmp_m--;
                } else {
                    tmp.push_back(nums2[k]);
                    k++;
                    tmp_n--;
                }
            }
        }
        

        nums1 = tmp;
    }
};