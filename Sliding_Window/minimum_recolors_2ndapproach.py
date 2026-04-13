class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        low = 0
        white_count = 0
        minimum_recolors = float('inf')

        for high in range(len(blocks)):
            # Add new element to window
            if blocks[high] == 'W':
                white_count += 1

            # Shrink window if size exceeds k
            while high - low + 1 > k:
                if blocks[low] == 'W':
                    white_count -= 1
                low += 1

            # Update answer when window size is exactly k
            if high - low + 1 == k:
                minimum_recolors = min(minimum_recolors, white_count)

        return minimum_recolors