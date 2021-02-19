# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:01:16 2021

@author: leo
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        """while(now!=len(nums)-1):
            if nums[now]==nums[now+1]:
                nums.pop(now)
            else:
                now+=1
        return len(nums),nums"""
        #now=-9
        if len(nums)==0:
                return 0
        count=0
        h=0
        while(h<len(nums)-1):
            if nums[h]!=nums[h+1]:
                nums[count]=nums[h]
                count+=1
            h+=1    
            #else:
                #nums.pop(h)
        nums[count]=nums[h]
        count+=1
        
        print(nums)
        return count
                
        
        
        
        
def main():
    side= Solution
    
    print(side.removeDuplicates(side,[1,2,3]))
    

if __name__ == "__main__":
    main()