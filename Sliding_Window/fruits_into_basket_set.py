# Problem: LeetCode 904 - Fruit Into Baskets
# Approach: Sliding Window using a List (Visual Method)

def total_fruit_list_version(arr):
    low = 0
    maximum = 0
    basket = []

    for high in range(len(arr)):
        # 1. Add the current fruit to our "window"
        basket.append(arr[high])

        # 2. Use set() to check if we have more than 2 distinct types
        while len(set(basket)) > 2:
            # 3. If so, remove from the front until we are back to 2 types
            basket.pop(0)
            low += 1
        
        # 4. Update our record-breaking length
        current_window_size = len(basket) # Or high - low + 1
        if current_window_size > maximum:
            maximum = current_window_size
            
    return maximum

# Test Case
example_orchard = [0, 1, 2, 2, 1, 3]
print(f"Maximum fruits you can collect: {total_fruit_list_version(example_orchard)}")

