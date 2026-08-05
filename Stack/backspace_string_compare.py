# leetcode 844
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]
    

        for i in range(len(s)):
            if s[i]!="#":
                s_stack.append(s[i])
            else:
                if s_stack:
                        s_stack.pop()

        for i in range(len(t)):
            if t[i]!="#":
                t_stack.append(t[i])
            else:
                if t_stack:
                    t_stack.pop()
                

        if s_stack==t_stack:
            return True
        else:
            return False



        