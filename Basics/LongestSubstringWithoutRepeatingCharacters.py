# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Dynamic sliding window

class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubString = 0
        currentSubString = ""

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            for windowEnd in range(len(s)):
                while s[windowEnd] in currentSubString:
                    currentSubString = currentSubString.replace(currentSubString[0], "")
                
                currentSubString += s[windowEnd]
                longestSubString = max(longestSubString, len(currentSubString))
        
            print(longestSubString)
            return longestSubString
        
test = Solution()
test.lengthOfLongestSubstring("abcabcbb")