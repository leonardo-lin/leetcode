# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:34:54 2021

@author: leo
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        while(i<len(nums)):
            if nums[i]>=target:
                return i
            i+=1
        return i
        
        
        
        
def main():
    side= Solution
    
    print(side.searchInsert(side,[1,3,5,6],4))
    

if __name__ == "__main__":
    main()