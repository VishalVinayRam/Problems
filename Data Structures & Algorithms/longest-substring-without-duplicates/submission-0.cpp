class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> mp;
        int k = 0;
        int max_seq = 0;
        for(int j=0;j<s.size();j++)
        {
            while(mp[s[j]]==1)
            {
                mp[s[k]]-=1;
                k+=1;
            }
            mp[s[j]]++;
            max_seq= max(max_seq,j-k+1);
        }
        return max_seq;
    }
};
