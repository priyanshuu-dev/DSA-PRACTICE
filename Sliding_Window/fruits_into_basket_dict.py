class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # State Management: basket tracks {fruit_type: count}
        basket = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            # Add current fruit to the basket
            current_fruit = fruits[right]
            basket[current_fruit] = basket.get(current_fruit, 0) + 1
            
            # Constraint: We can only have 2 types of fruit
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                
                # If count hits zero, remove the fruit type entirely
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                
                # Shrink the window from the left
                left += 1
            
            # Update the global maximum window size
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits