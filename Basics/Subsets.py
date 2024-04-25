
def subsets(nums):
    res = []

    current_subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(current_subset.copy())
            return
        
        # descision to include nums[i]
        current_subset.append(nums[i])
        dfs(i + 1)

        current_subset.pop()
        dfs(i+1)
    
    dfs(0)
    return res

print(subsets([1,2,3]))


        