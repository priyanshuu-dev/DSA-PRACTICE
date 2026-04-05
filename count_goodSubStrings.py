class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        low = 0
        window = []

        for high in range(len(s)):
            # expand window
            window.append(s[high])

            # when window size becomes 3
            if high - low + 1 == 3:
                
                # check if all characters are distinct
                if len(set(window)) == 3:
                    count += 1

                # shrink window
                window.pop(0)
                low += 1

        return count





    

