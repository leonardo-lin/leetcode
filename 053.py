# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:25:40 2021

@author: leo
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]
        now=0
        for i in nums:
            if now<0:
                now=0
            now+=i
            print(now)
            ans=max(ans,now)
        
        return ans
     
def main():
    side= Solution
    #print(p=='apple')
    #print(side.strStr(side,'hello','ll'))
    print(side.maxSubArray(side,[1]))
    
    
    

if __name__ == "__main__":
    main()