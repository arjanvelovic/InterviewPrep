import math

def search(nums, target):

    left = 0
    right = len(nums)-1
    
    while left<=right:
        mid = math.floor((left+right)/2)
        if nums[mid]==target:
            return mid
        elif nums[mid] > target:
            if nums[left] <= target and nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

print(search([[4,5,6,7,0,1,2]], 0))