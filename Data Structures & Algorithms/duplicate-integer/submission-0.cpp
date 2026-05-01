class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> result(nums.begin(),nums.end());
        if(result.size()==nums.size())
        {
            return false;
        }
        return true;
    }
};
