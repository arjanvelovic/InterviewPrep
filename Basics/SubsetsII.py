testarray = [0,1,2,3]

def subsetsWithDup(nums):
    subsets = []
    if len(nums) == 0:
        return subsets
    elif len(nums) == 1:
        print(f'last num: {nums[0]}')
    else:
        for i in range(len(nums)):
            currentnum = nums[i]
            remainingnums = nums[i+1:]
            print(f"current num: {currentnum}")
            print(f"remaining nums: {remainingnums}")

            subsetsWithDup(remainingnums)

subsetsWithDup(testarray)