class Solution(object):
    def isSubsequence(self, s, t):
        target=0
        scout=0
        while scout<len(t) and target<len(s):
            #matched
            if s[target]==t[scout]:
                scout+=1
                target+=1
            else:
                scout+=1
        if target==len(s):
            return True
        else:
            return False
