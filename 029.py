# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:38:53 2021

@author: leo
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans=dividend//divisor
        if ans>2147483647 or ans<-2147483648:
            return 2147483647
        if dividend%divisor==0:
            return ans
        elif ans<0:
            return ans+1
        return ans
        
        
def main():
    side= Solution
    
    print(side.divide(side,-2147483648,-1))
    

if __name__ == "__main__":
    main()