class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while r>=l:
            if s[l].isalnum() is  False:
                l+=1
                continue
            if s[r].isalnum() is False:
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                print(s[l])
                print(s[r])
                return False
            l+=1
            r-=1
        return True
