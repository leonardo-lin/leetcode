# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:37:19 2021

@author: leo
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n>0:
            tmp=1
            #n-=1
            while(n>1):
                if(n%2==0):
                    x=x*x
                    n/=2
                else:
                    tmp*=x
                    n-=1
                    
            return x*tmp
        else:
            ans=1/x
            n=-n
            tmp=1
            while(n>1):
                if(n%2==0):
                    ans*=ans
                    n/=2
                else:
                    tmp*=ans
                    n-=1
            return ans*tmp
            
            
            
            


def main():
    side= Solution
    
    print(side.myPow(side,2,-8))
    
    
    

if __name__ == "__main__":
    main()