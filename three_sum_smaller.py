def count_triplets(nums, target):
    nums.sort()
    ans = 0
    
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < target:
                # All numbers between left and right work!
                ans += (right - left)
                left += 1
            else:
                right -= 1
                
    return ans

# --- Testing the code ---
nums = [-2, 0, 1, 3]
target = 2
print(f"Triplets found: {count_triplets(nums, target)}")
    



        
            


