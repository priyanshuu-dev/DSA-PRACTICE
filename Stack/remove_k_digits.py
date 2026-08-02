#leetcode 402
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
        stack=[]
     
        res=""
        for i in range(len(num)):

            while stack and k>0 and stack[-1]>num[i]: 
                stack.pop()
                k-=1

            stack.append(num[i])

        for i in range(len(stack)):
            res+=stack[i]
        if stack and k!=0:
            while stack and k:
                stack.pop()
                k-=1 
        
        res="".join(stack)
        i=0

        while i <len(res) and res[i]=='0':
            i+=1
        res=res[i:]

        if res=="":
            return "0"
        return res