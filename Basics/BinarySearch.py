def search(nums, target):

    maxindex = len(nums)
    minindex = 0

    def binarysearch(minindex, maxindex):
        midpoint = (minindex + maxindex) // 2

        if target == nums[midpoint]:
            return midpoint
        elif len(nums[minindex:maxindex]) == 1:
            return -1
        elif target > nums[midpoint]:
            minindex = midpoint
        elif target < nums[midpoint]:
            maxindex = midpoint
        return binarysearch(minindex, maxindex)
    
    return binarysearch(minindex, maxindex)

def search2(nums, target):

    left = 0
    right = len(nums)-1
    
    while left<=right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right = mid-1
        else:
            left = mid+1
    
    return -1

print(search([0,1,2,3,4,5],4))
print(search2([0,1,2,3,4,5],4))
            
        