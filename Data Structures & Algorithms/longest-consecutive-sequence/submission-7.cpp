class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

       vector<int> result;
       sort(nums.begin(),nums.end());
       if(nums.size()==0 || nums.size()==1)
       {
        return nums.size();
       }
       int current_small = nums[0];
       int count =1;
       int maxs =1;
       for(int i=1;i<nums.size();i++)
       {
        if(current_small==nums[i])
        {
            continue;
        }
        else if(current_small!=nums[i]-1)
        {
            maxs = max(maxs,count);
            count = 1;
            current_small = nums[i];
        }
        else
        {
            current_small = nums[i];
            count+=1;
            maxs = max(maxs,count);
        }
       }
       if(maxs==0)
       {
        return 0;
       }
       return maxs;
    }
};
