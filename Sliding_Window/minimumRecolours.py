class Solution(object):
    def minimumRecolors(self, blocks, k):
        count = 0
        
        # Step 1: first window
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        
        ans = count
        
        # Step 2: slide window
        for i in range(k, len(blocks)):
            
            # remove left element
            if blocks[i - k] == 'W':
                count -= 1
            
            # add right element
            if blocks[i] == 'W':
                count += 1
            
            # update answer
            ans = min(ans, count)
        
        return ans