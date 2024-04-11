# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# current solution takes too long, need to use center out two pointer solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = ""

        for character in s:
            if character.isalnum():
                newstring += character.lower()

        for i in range(len(newstring)):
            print(f"{newstring[i]}, {newstring[-(i+1)]}")
            if newstring[i] != newstring[-(i+1)]:
                return False
        
        return True

        # StringFront = 0
        # StringEnd = 1
        # if len(s) <= 1:
        #     return True
        # else:
        #     while StringFront <= len(s)/2 and StringEnd <= len(s)/2:
        #         while s[StringFront].isalnum() == False:
        #             StringFront += 1
        #         while s[-StringEnd].isalnum() == False:
        #             StringEnd += 1
        #         print(f"{s[StringFront]}, {s[-StringEnd]}")
        #         if s[StringFront].lower() != s[-StringEnd].lower():
        #             return False
        #         StringFront += 1
        #         StringEnd += 1
        
        # return True

test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))