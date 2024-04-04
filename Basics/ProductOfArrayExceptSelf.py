# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

#use of two pointers and muilitple for loops running in conjunction

class Solution():
    def productExceptSelf(self, nums) -> [int]:
        n = len(nums)
        productArray = []
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(n):
            productArray.append(prefix[i]*suffix[i])
        
        print(productArray)
        return productArray

test = Solution()
test.productExceptSelf(nums=[1,2,3,4])