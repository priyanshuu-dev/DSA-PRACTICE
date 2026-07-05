class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        smallest=high
        while low<=high:
            guess=(low+high)//2
            hours=0
            for p in piles:
                if p % guess == 0:
                   hours += p // guess
                else:
                    hours += p // guess + 1
                


            if hours<=h:
                smallest=min(smallest,guess)
                high=guess-1
            else:
                low=guess+1
        return smallest