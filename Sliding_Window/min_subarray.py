def min_subarray_len(target, arr):
    low = 0
    high = 0
    total = 0
    size = float('inf')

    while high < len(arr):
        total += arr[high]

        while total >= target:
            current_window = high - low + 1
            
            if current_window < size:
                size = current_window

            total -= arr[low]
            low += 1
        
        high += 1

    return size if size != float('inf') else 0

# Test
print(min_subarray_len(4, [1, 2, 4, 4]))
    


