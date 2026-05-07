class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> temp_result;
        map<int,vector<int>> maps;
        for(int i =0;i<nums.size();i++)
        { 
            maps[nums[i]].push_back(i);
        }
        for(int i=0;i<nums.size();i++)
        {
            for(int j =i;j<nums.size();j++)
            {
                if(i==j)
                {
                    continue;
                }
                int target = -(nums[i]+nums[j]);
                if(maps.count(target))
                {
                    for(int k =0;k<maps[target].size();k++)
                    {
                        if(maps[target][k]==i || maps[target][k]==j)
                        {
                            continue;
                        }
                        vector<int> unsorted_list;
                        unsorted_list.push_back(nums[i]);
                        unsorted_list.push_back(nums[j]);
                        unsorted_list.push_back(nums[maps[target][k]]);
                        sort(unsorted_list.begin(),unsorted_list.end());
                        temp_result.insert(unsorted_list);
                        break;
                    }
                }
            }
        }
        vector<vector<int>> result;
        for(auto &x : temp_result)
        {
            result.push_back(x);
        }
        return result;
    }
};