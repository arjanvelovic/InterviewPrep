import math
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        i = 0

        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            l_p = i + 1
            r_p = len(nums) - 1

            while l_p < r_p:
                total = nums[i] + nums[l_p] + nums[r_p]

                if total == 0:
                    triplets.append([nums[i],nums[l_p],nums[r_p]])
                    l_p += 1
                    while nums[l_p] == nums[l_p - 1] and l_p < r_p:
                        l_p += 1
                elif total > 0:
                    r_p -= 1
                else:
                    l_p += 1
                    while nums[l_p] == nums[l_p - 1] and l_p < r_p:
                        l_p += 1
            
            i += 1
            while nums[i] == nums[i - 1] and i < len(nums) - 2:
                i += 1
        
        return triplets




        
        