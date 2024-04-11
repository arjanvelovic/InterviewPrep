# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Fixed sliding window

class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        maxAverage = -10000
        currentAverage = 0
        currentSum = 0

        if len(nums) <= 1:
            return nums[0]
        else:
            for i in range(len(nums)):
                currentSum += nums[i]

                if i >= k-1:
                    maxAverage = max(maxAverage, currentSum/k)
                    currentSum -= nums[i-k+1]

        return maxAverage
    
test = Solution()
print(test.findMaxAverage([1,12,-5,-6,50,3], 4))