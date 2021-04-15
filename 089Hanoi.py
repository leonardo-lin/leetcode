
t=0
class Solution(object):
    #t=0
    #ans=[]
    """def __init__(self,t):
        self.t=t
    def Hanoi(self,n,ans,a):
        
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
            self.Hanoi(n-1,ans,-a)"""
        #return ans
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        
        """
        
        answer=[0]
        def Hanoi(n,ans,a):
            global t
            if n==0:
                
                ans.append(t+(2**n)*a)
                t=(t+(2**n)*a)
                print((2**n)*a,ans)
                print()
            else:
                b=a
                if b<0:
                    b=-b
                print(b)
                Hanoi(n-1,ans,b)

                ans.append(t+(2**n)*a)
                t=t+(2**n)*a
                print((2**n)*a,ans)
                print()

                Hanoi(n-1,ans,-b)
        
        Hanoi(n-1,answer,1)
        
        return answer
  
def main():
    side= Solution
    #print('hi')
    print(side.grayCode(side,3))
    ans=[]
    #print(side.Hanoi(side,3,ans))
    #Hanoi()
    
    
    

if __name__ == "__main__":
    main()