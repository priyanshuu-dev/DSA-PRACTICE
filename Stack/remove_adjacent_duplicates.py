#leetcode 1047

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        

        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        ans=""

        for i in range(len(stack)):
            ans+=stack[i]

    
        return ans