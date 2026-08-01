class Solution:
	def preGreaterEle(self, arr):
		
		stack=[]
		res=[-1] * len(arr)
		n=-1*(len(arr))
		n-=1
		
		for i in range(-1,n,-1):
		    
		    while stack and arr[i] > arr[stack[-1]]:
		        a=stack.pop()
		        res[a]=arr[i]
		        
		        
		    stack.append(i)
		    
		    
		    
		return res