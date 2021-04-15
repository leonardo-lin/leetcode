

class Solution(object):
    #ans=[]
    """def __init__(self,t):
        self.t=t
    def Hanoi(self,n,ans,a):
        side =Solution
        if n==0:
            
            ans.append(self.t+(2**n)*a)
            self.t=(self.t+(2**n)*a)
            print(n*a,ans)
            print()
        else:
            self.Hanoi(n-1,ans,a)
            ans.append(self.t+(2**n)*a)
            self.t=self.t+(2**n)*a
            print(n*a,ans)
            print()
            self.Hanoi(n-1,ans,-a)
        #return ans"""
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        
        """
        
        minus=[1 for x in range(n)]
        answer=[0]
        t=0
        i=1
        while i < (2**(n)):
            j=2**(n-1)
            count=n-1
            while(j>0):
                if i%j==0:
                    #print(i,j,i%j)
                    
                    
                    answer.append(t+j*(minus[count]))
                    #print('append',t+(j*(minus[count])))
                    t=t+j*(minus[count])
                    minus[count]*=-1
                    #print(minus[count],count,j)
                    #print()
                    break
                j/=2
                count-=1
            i+=1
        return answer
  
def main():
    side= Solution
    #print('hi')
    print(side.grayCode(side,4))
    ans=[]
    #print(side.Hanoi(side,3,ans))
    #Hanoi()
    
    
    

if __name__ == "__main__":
    main()