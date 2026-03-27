# Function to find max sum of 2 adjacent numbers
def get_max_sum(arr):
    low = 0
    high = 1
    
    # Calculate the first window
    current_sum = arr[low] + arr[high]
    max_sum = current_sum
    
    # Slide the window until high reaches the end
    while high < len(arr) - 1:
        # 1. Remove the old 'low' value
        current_sum = current_sum - arr[low]
        
        # 2. Move pointers forward
        low = low + 1
        high = high + 1
        
        # 3. Add the new 'high' value
        current_sum = current_sum + arr[high]
        
        # 4. Check if we found a bigger sum
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum

# Test with your array
nums = [1, 2, 3, 4]
result = get_max_sum(nums)

print("Maximum sum found:")
print(result)
   


    