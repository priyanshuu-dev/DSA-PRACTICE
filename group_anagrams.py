class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        dd=defaultdict(list)
        for ch in strs:
            key="".join(sorted(ch))
            dd[key].append(ch)
        return(list(dd.values()))