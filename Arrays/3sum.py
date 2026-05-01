def three_sum(nums):
    """
    Finds all unique triplets in the array which gives the sum of zero.
    """
    nums.sort()
    results = []
    
    for i in range(len(nums)):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i + 1, len(nums) - 1
        
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                results.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                # Skip duplicate values for the second and third elements
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
    return results

# Example usage:
arr = [-1, -1, 0, 1, 2, 4]
print(three_sum(arr))




