class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        result=[]

        i=0
        j=0

        while i<len(a) and j<len(b):
            s1=a[i][0]
            e1=a[i][1]

            s2=b[j][0]
            e2=b[j][1]

            if e1>=s2  and e2>=s1:
                s=max(s1,s2)
                e=min(e1,e2)
                result.append([s,e])

            if e1<e2:
                i+=1
            elif e1>e2:
                j+=1
            else:
                i+=1
                j+=1

        return result
