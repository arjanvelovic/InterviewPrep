class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 
        elif len(s) == 1:
            return s

        res = ""

        for i in range(len(s)):
            l = i
            r = i

            while s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

                if l < 0 or r > len(s) - 1:
                    break
            
            l = i
            r = i + 1

            if r < len(s):
                while s[l] == s[r]:
                    if (r - l + 1) > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1

                    if l < 0 or r > len(s) - 1:
                        break

        return res
        