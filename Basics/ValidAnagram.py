# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Frequency count

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = "abcdefghijklmnopqrstuv"

        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        
        return True
    
test = Solution()
print(test.isAnagram("anagram", "nagaram"))