class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        count=float('inf')
        left,right,answer=[None]*n,[None]*n,[None]*n
        for i in range(n):
            if s[i] == c:
                count=0
            left[i]=count
            count+=1
        count=float('inf')
        for i in range(n-1,-1,-1):
            if s[i] == c:
                count=0
            right[i]=count
            count+=1
        for i in range(n):
            answer[i]=min(right[i],left[i])
        return answer
        
